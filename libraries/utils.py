import json


def save_to_json(filename, content):
    json_data = json.dumps(content)
    with open("./site/"+filename, 'w') as f:
        f.write("var JSON = "json_data)
