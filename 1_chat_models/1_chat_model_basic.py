# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import openai
import os

# Load environment variables from .env
load_dotenv(override=True)

# Set OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# print(os.getenv("OPENAI_API_KEY") , " 1231231231231123132 ")

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
