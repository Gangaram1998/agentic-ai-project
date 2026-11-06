from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings :
    api_key:str = os.getenv('API_KEY', "")
    model:str = os.getenv("MODEL_NAME", "")
    max_steps:int = int(os.getenv("MAX_STEPS", ""))
    timeout_s:int = 30


setting = Settings()
if not setting.api_key :
    raise RuntimeError("API_KEY is required.")