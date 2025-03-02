from utils.gemini_api import get_gemini_response

def evaluate_resume_fit(input_text, pdf_content):
    """
    Evaluates the resume's fit with the job description by providing strengths and weaknesses.
    """
    input_prompt = """
    You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description.
    Please share your professional evaluation on whether the candidate's profile aligns with the role.
    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    """
    response = get_gemini_response(input_text, pdf_content, input_prompt)
    return response

def evaluate_percentage_match(input_text, pdf_content):
    """
    Evaluates the resume's match percentage against the job description.
    """
    input_prompt = """
    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
    Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
    the job description. First, the output should come as a percentage, followed by keywords missing, and then final thoughts.
    """
    response = get_gemini_response(input_text, pdf_content, input_prompt)
    return response
