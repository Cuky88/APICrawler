import json
import codecs

def read(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data

def write(path, data):
    json_db = json.dumps(data , codecs.open(path, 'w', encoding='utf-8'),separators=(',', ':'), indent=4)
    with open(path, "w") as f:
        f.write(json_db)
