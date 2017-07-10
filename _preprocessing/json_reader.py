import json

def load(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data

