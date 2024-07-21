import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from src.tweetcrafter_crew.callbacks import LLMCallbackHandler
from src.tweetcrafter_crew.config import Config, Model


def create_model(model: Model):
    callback = LLMCallbackHandler(Config.Path.LOGS_DIR / "prompts.jsonl")
    if model == Model.LLAMA_3:
        return ChatGroq(
            model="llama3-70b-8192", 
            groq_api_key=os.getenv('GROQ_API_KEY'), 
            callbacks=[callback])
    
    elif model == Model.GPT_4o:
        return ChatOpenAI(
            model_name="gpt-4o", 
            callbacks=[callback])