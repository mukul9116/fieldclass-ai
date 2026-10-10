import ollama 
from pydantic import ValidationError,BaseModel
import httpx
import logging

logger = logging.getLogger(__name__)

from fieldclass.config import get_profile,ModelProfile

class LLMUnavailable(Exception):
    """Ollama cannot be reached or Model is missing"""

class LLMOutputError(Exception):
    """The Model answered but that was un-usable"""

def ask_once(messages: list[dict], schema: type[BaseModel], profile: ModelProfile) -> BaseModel:
    client = ollama.Client(timeout = profile.timeout_s)
    try:
        response = client.chat(
            model= profile.model,
            messages = messages,
            format = schema.model_json_schema(),
            options={
                "temperature": profile.temperature,
                "num_predict": profile.num_predict,
                "num_ctx": profile.num_ctx
            },

        )
    
    except ollama.ResponseError as e:
        if e.status_code == 404:
            raise LLMUnavailable(f"Model '{profile.model}' is not installed. Run: ollama pull {profile.model}") from e
        
        if e.status_code == 500:
            raise LLMOutputError(f"Ollama could not finish the answer (500): {e.error}") from e
        
        raise LLMUnavailable(f"Ollama returned an error ({e.status_code}): {e.error}") from e
    
    if(response.done_reason == "length"):
        raise LLMOutputError("The answer was cutoff due to token limit!")

    raw  = response.message.content or ""
    try:
        return schema.model_validate_json(raw)
    except ValidationError as e:
        raise LLMOutputError(f"The answer didnt match the expected form: {e}") from e 

def generate_structured(messages: list[dict],schema:type[BaseModel], profile:ModelProfile | None = None, max_retries:int = 2) -> BaseModel:
    profile = profile or get_profile()
    last_error = None 
    for attempt in range(max_retries + 1):
        try:
            return ask_once(messages, schema, profile)
        except LLMOutputError as e:
            last_error = e
            logger.warning("Attempt %s failed: %s", attempt + 1, e)
    raise LLMOutputError(f"Gave up after {max_retries + 1} attempt. Last Problem: {last_error}")



    