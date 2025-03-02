import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")