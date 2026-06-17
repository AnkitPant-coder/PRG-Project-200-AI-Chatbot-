import google.generativeai as genai
import os
from memory import get_memories
from rag import search_documents
from dotenv import load_dotenv 

load_dotenv()

genai.configure(
    api_key=os.getenv ("AQ.Ab8RN6KvDMgt28PjC7M3jOuAnl8z-q6mYPAAT_a1j57OZ5Pg3g")
)

MODEL_NAME = "gemini-2.5-flash"

model = genai.GenerativeModel(MODEL_NAME)


def generate_response(user_input):

    docs = search_documents(user_input)

    memories = get_memories()

    prompt = f"""
You are an intelligent AI assistant.

Use the conversation memory and retrieved knowledge when relevant.

Conversation Memory:
{chr(10).join(memories)}

Knowledge Base:
{chr(10).join(docs)}

User Question:
{user_input}

Provide a helpful and natural answer.
"""

    try:

        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text

        return str(response)

    except Exception as e:

        return f"Gemini Error: {str(e)}"