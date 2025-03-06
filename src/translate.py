import os
import random



import openai
from langchain.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

openai.api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
source_lang = 'english'
target_lang = 'russian'

prompt =  f"""You are a professional translator from {source_lang} to {target_lang}.
Translate the input text into {target_lang} maintaining the original meaning, tone, and formatting.
Provide ONLY the translation without explanations, notes, or original text unless specifically requested.
For specialized terminology, use the appropriate {target_lang} domain-specific terms."""





import os
import requests
import json

def create_translator(api_key=None, source_lang="English", target_lang="Russian", model="gpt-3.5-turbo"):
    """
    Creates a translator function that uses direct OpenAI API calls.
    
    Args:
        api_key (str, optional): OpenAI API key. Defaults to environment variable.
        source_lang (str, optional): Source language. Defaults to "English".
        target_lang (str, optional): Target language. Defaults to "Russian".
        model (str, optional): OpenAI model to use. Defaults to "gpt-3.5-turbo".
        
    Returns:
        function: A translation function
    """
    # Use provided API key or get from environment
    openai_api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key must be provided or set as OPENAI_API_KEY environment variable")
    
    # Set up system message for translation
    system_message = f"""You are a professional translator from {source_lang} to {target_lang}.
Translate the input text into {target_lang} maintaining the original meaning, tone, and formatting.
Provide ONLY the translation without explanations, notes, or original text unless specifically requested.
For specialized terminology, use the appropriate {target_lang} domain-specific terms."""
    
    def translate_text(text):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ],
            "temperature": 0.1  # Low temperature for consistent translations
        }
        
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        if response.status_code == 200:
            result = response.json()
            translated_text = result["choices"][0]["message"]["content"].strip()
            return translated_text
        else:
            error_message = f"API Error {response.status_code}: {response.text}"
            raise Exception(error_message)
    
    return translate_text

def load_quiz_db(quize_db_path):
    if not os.path.exists(quize_db_path):
        return {}
    with open(quize_db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def dump_quiz_db(data, quize_db_path):
    with open(quize_db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    


current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
quiz_file_path = os.path.join(current_dir, 'quiz.txt')
quize_db_path = os.path.join(current_dir, 'quiz_db.json')

quize_db = load_quiz_db(quize_db_path)
non_empty_lines = []
with open(quiz_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        stripped_line = line.strip()
        if len(stripped_line) > 0:
            non_empty_lines.append(stripped_line)
print(f'Num questions loaded {len(non_empty_lines)}')

print(random.choice(non_empty_lines))

human_input = f"""
Please translate the following English text to Russian:

{line}

Please provide only the translation without additional explanations unless I specifically ask for clarification about certain words or phrases.
"""

eng_to_rus_translator = create_translator()

for line in non_empty_lines:
    if line not in quize_db:
        translation = eng_to_rus_translator(line)
        quize_db[line] = translation.strip()
dump_quiz_db(quize_db, quize_db_path)