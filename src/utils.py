import json
import os

import requests

def load_json(json_path):
    if not os.path.exists(json_path):
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def dump_json(data, quize_db_path):
    with open(quize_db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_file_path(file_name):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    file_path = os.path.join(current_dir, file_name)
    return file_path

def create_translator(api_key=None, source_lang="English", target_lang="Russian", model="gpt-3.5-turbo"):
    openai_api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key must be provided or set as OPENAI_API_KEY environment variable")
    if source_lang == target_lang == 'English':
        system_message =         """
            You are a professional translator specializing in corporate communications. Your task is to:

            1. First, provide an English translation with just fixing errors in the original message.
            2. Then, provide 3 alternative phrasings of the translated text, maintaining the same professional tone but using different vocabulary and sentence structures
            3. Each alternative should convey the same meaning but use different expressions common in business communication
            4. Ensure all versions maintain a formal, professional tone suitable for corporate environments

            Format your response as follows:

            PRIMARY TRANSLATION:
            > [Your main translation in polished corporate English]

            ALTERNATIVE PHRASINGS:
            > [First alternative phrasing]
            > [Second alternative phrasing]

            Remember to:
            - Use contemporary business vocabulary
            - Maintain consistency in tone across all versions
            - Ensure each alternative offers a fresh perspective while preserving the original meaning
            - Keep the language clear and accessible for international business audiences
        """
    else:
        system_message = f"""You are a professional translator from {source_lang} to {target_lang}.
    Translate the input text into {target_lang} maintaining the original meaning, tone, and formatting.
    Provide ONLY the translation without explanations, notes, or original text unless specifically requested.
    For specialized terminology, use the appropriate {target_lang} domain-specific terms."""
    
    def translate_text(user_prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
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
