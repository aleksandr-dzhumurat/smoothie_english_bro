import json
import os

from gemini_adapter import generate_text


def load_json(json_path):
    if not os.path.exists(json_path):
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def dump_json(data, quize_db_path):
    with open(quize_db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_jsonl(jsonl_path):
    if not os.path.exists(jsonl_path):
        return []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def append_jsonl(record, jsonl_path):
    with open(jsonl_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

def get_file_path(file_name):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    file_path = os.path.join(current_dir, file_name)
    return file_path

def create_translator(source_lang="English", target_lang="Russian"):
    if source_lang == target_lang == 'English':
        system_message = """
            You are a professional translator specializing in corporate communications. Your task is to:

            Critical: if input text is a question, then just fix errors in the original message, do not answer.
            
            If input text is not a question, then do the following:
            
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
        return generate_text(system_message, user_prompt)

    return translate_text
