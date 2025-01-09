import os

from config.config import OpenAIConfig

open_ai_config = OpenAIConfig(
    api_key=os.getenv("OPENAI_API_KEY")
)
