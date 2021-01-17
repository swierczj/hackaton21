import json


NUM_OF_ANS = 2
NUM_OF_CHAR = 500
SITE = "stackoverflow.com"
AUTO = True


def save_to_json(filename, content):
    json_data = json.dumps(content)
    with open("./site/"+filename, 'w') as f:
        f.write("var JSON = "+json_data)


def load_config(filename):
    with open(filename) as config_file:
        data = json.load(config_file)
        NUM_OF_ANS = data['number_of_answers_for_error']
        NUM_OF_CHAR = data['number_of_characters_in_tooltip']
        SITE = data['results_from_site']
