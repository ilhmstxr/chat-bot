from google import genai
import os
from dotenv import load_dotenv


api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(model="gemini-2.5-pro")

def chat_inference(prompt):
    response = chat.send_message(prompt)
    return response.text

# if __name__ == "__main__":
  
# input_text = input("Chat: ")
# chat_inference(input_text)
# print("Response:", chat_inference(input_text))