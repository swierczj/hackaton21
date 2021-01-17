import json
import libraries.config as config


def save_to_json(filename, content):
    json_data = json.dumps(content)
    with open("./site/"+filename, 'w') as f:
        f.write("var JSON = "+json_data)


def load_config(filename):
    with open(filename) as config_file:
        data = json.load(config_file)
        config.NUM_OF_ANS = data['number_of_answers_for_error']
        config.NUM_OF_CHAR = data['number_of_characters_in_tooltip']
        config.SITE = data['results_from_site']
        config.AUTO = data['automatic_search']
