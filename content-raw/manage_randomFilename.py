import os
import random
import string
import json

JSON_FILE = f"{os.path.dirname(os.path.abspath(__file__))}/file_mapping.json"           # CSVファイルの保存先

def _generate_random_string(length=10):
    """指定された長さのランダムな文字列を生成"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def get_randomized_dir_name(source_name):
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)  # JSONを辞書形式で読み込む
    
    keys_list = list(data.keys())

    if source_name in keys_list:
        return data[source_name]

    return None

def generate_randomized_dir_name(source_name):
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)  # JSONを辞書形式で読み込む
    
    if get_randomized_dir_name(source_name):
        return data[source_name]

    random_name = _generate_random_string()

    data[source_name] = random_name

    
    # 対応表をJSONファイルに保存
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # 辞書をJSON形式で保存

    return random_name
