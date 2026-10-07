import os
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelProfile:
    name:str
    model:str
    temperature:float
    num_predict:int
    num_ctx:int 
    timeout_s:float

PROFILES = {
    "lite" : ModelProfile(
        name = "lite",
        model = "gemma3:1b",
        temperature  =  0.4,
        num_predict =  300,
        num_ctx =  2048,
        timeout_s = 60.0,
    ),
}

DEFAULT_PROFILE = "lite"

def get_profile(name: str | None = None) -> ModelProfile:
    if(name is None):
        name = os.environ.get("fieldclass_profile", DEFAULT_PROFILE)
    if(name not in PROFILES):
        available = ", ".join(PROFILES)
        raise ValueError(f"unknown profile '{name}'. available PROFILES: {available}")
    return PROFILES[name]


