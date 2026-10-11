#!/bin/bash
ollama serve &
until ollama list > /dev/null 2>&1; do
  sleep 1
done
ollama pull gemma3:1b
wait