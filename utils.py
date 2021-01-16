import json


def save_to_json(filename, content):
    json_data = json.dumps(content)
    with open(filename, 'w') as f:
        f.write(content)
