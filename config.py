from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_TOKEN_BOT = os.environ.get("api_token_bot")
API_TOKEN_CONVERT = os.environ.get("api_token_convert")