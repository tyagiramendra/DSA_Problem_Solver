import os

from dotenv import load_dotenv
load_dotenv()

MODEL_NAME ="gpt-4o"
MAX_TURN=10
TERMINATION_TEXT="STOP"
TEMPERATURE=0
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")