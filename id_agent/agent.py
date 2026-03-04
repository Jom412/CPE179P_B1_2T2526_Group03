from google.adk.agents import Agent
import datetime

# --- TOOL 1: CHECK FOR DUPLICATES ---
def search_duplicate_identity(full_name: str, id_number: str) -> dict:
    """
    Checks the database to see if this person already exists.
    
    Args:
        full_name: The name extracted from the ID.
        id_number: The ID number extracted.
    """
    print(f"\n[System] 🔍 Searching database for: {full_name} ({id_number})...")
    
    if "Juan Dela Cruz" in full_name:
        return {
            "is_duplicate": True, 
            "match_confidence": 0.98, 
            "existing_record": "REF-8821"
        }
    
    return {"is_duplicate": False, "match_confidence": 0.1}

# --- TOOL 2: SUMMARIZE & VALIDATE ---
def validate_and_summarize(expiry_date: str) -> dict:
    """
    Validates if the ID is expired and returns a status summary.
    
    Args:
        expiry_date: The expiry date found on the ID (Format YYYY-MM-DD).
    """
    print(f"\n[System] 📅 Validating expiry date: {expiry_date}...")
    
    try:
        exp = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")
        if exp < datetime.datetime.now():
            return {"status": "REJECTED", "reason": "Document is Expired"}
        else:
            return {"status": "ACCEPTED", "reason": "Document is Active"}
    except:
        return {"status": "ERROR", "reason": "Invalid Date Format"}

# --- THE AGENT CONFIGURATION ---
root_agent = Agent(
    model='gemini-2.5-flash',
    name='id_verification_agent',
    description='An agent that extracts ID data and checks for duplicates.',
    instruction="""
    You are an automated Identity Document Processor.
    
    Your goal is to process an uploaded ID and output a final decision.
    
    STEPS:
    1. Read the ID image (or text description) to find: Name, ID Number, Expiry Date.
    2. CALL TOOL: `validate_and_summarize` to check if the ID is expired.
    3. CALL TOOL: `search_duplicate_identity` to check if the user exists.
    4. OUTPUT: A final summary block stating if the application is APPROVED or REJECTED.
    """,
    tools=[search_duplicate_identity, validate_and_summarize]
)