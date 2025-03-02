import google.generativeai as genai
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(input, pdf_content, prompt):
    """
    Sends a request to the Gemini API and returns the response text.
    """
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text
