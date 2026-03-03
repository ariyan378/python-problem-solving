from pprint import pprint

import json
def load_json_data(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

result = load_json_data("demo.json")
pprint(result)