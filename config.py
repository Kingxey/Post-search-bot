

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Optional: Set default values
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))
