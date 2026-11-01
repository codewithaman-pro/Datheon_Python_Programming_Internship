import re
import json
import os

def load_faq_data():
    """
    Loads FAQ data using exact absolute paths to avoid directory mismatch issues.
    """
    # Checking inside Code folder first, then main project folder
    file_path = r"C:\Users\dell\OneDrive\Documents\Python Hangman Internship\Code\sample_faq (2).json"
    
    if not os.path.exists(file_path):
        file_path = r"C:\Users\dell\OneDrive\Documents\Python Hangman Internship\sample_faq (2).json"

    if not os.path.exists(file_path):
        print(f"Warning: JSON file not found. Using default fallback data.")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def get_bot_response(user_input, faq_data):
    """
    Parses user input using regular expressions and matches against JSON FAQ data.
    """
    cleaned_input = user_input.lower().strip()
    
    if not faq_data:
        return "I am sorry, the knowledge base is currently unavailable."

    # Check for greetings from JSON
    for greeting in faq_data.get("greetings", []):
        if re.search(r'\b' + re.escape(greeting) + r'\b', cleaned_input):
            return "Hello! Welcome to the support assistant. How can I help you with your internship today?"

    # Check against FAQs in the JSON file
    for faq in faq_data.get("faqs", []):
        question = faq.get("question", "").lower()
        keywords = [word for word in re.findall(r'\w+', question) if len(word) > 3]
        
        match_count = sum(1 for kw in keywords if kw in cleaned_input)
        if match_count >= 2 or any(kw in cleaned_input for kw in keywords[:2]):
            return faq.get("answer")

    # Fallback response for unrecognized queries
    return "I am sorry, I didn't get that. Could you please rephrase your question or type 'help'?"

def run_chatbot():
    print("==================================================")
    print("      RULE-BASED TERMINAL ASSISTANT / CHATBOT     ")
    print("==================================================")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.\n")
    
    faq_data = load_faq_data()

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
                
            # Check for exit commands
            if user_input.lower() in ['bye', 'exit', 'quit']:
                print("Bot: Thank you for reaching out. Goodbye!")
                break
                
            response = get_bot_response(user_input, faq_data)
            print(f"Bot: {response}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session terminated. Goodbye!")
            break

if __name__ == "__main__":
    run_chatbot()