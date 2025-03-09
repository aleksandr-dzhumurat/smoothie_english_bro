import os
import random
import os

from utils import load_json, dump_json, create_translator


if __name__ == '__main__':
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    quiz_file_path = os.path.join(current_dir, 'quiz.txt')
    quize_db_path = os.path.join(current_dir, 'quiz_db.json')

    quize_db = load_json(quize_db_path)
    non_empty_lines = []
    with open(quiz_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                non_empty_lines.append(stripped_line)
    print(f'Num questions loaded {len(non_empty_lines)}')

    print(random.choice(non_empty_lines))

    eng_to_rus_translator = create_translator()

    for line in non_empty_lines:
        if line not in quize_db:
            translation = eng_to_rus_translator(line)
            quize_db[line] = translation.strip()
    dump_json(quize_db, quize_db_path)