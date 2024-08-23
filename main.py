import requests
import json
import datetime
import os

def make_api_call(base_url, api_key, pse_key, extra_params, query_param, param_value):

    url = f"{base_url}{api_key}{pse_key}{extra_params}&{query_param}={param_value}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(url)
        print(f"Error: {response.status_code} - {response.reason}")
        return None

with open("config.json") as config_file:
    config = json.load(config_file)

base_url = "https://www.googleapis.com/customsearch/v1"
api_key = "?key=" + config['API_KEY']
pse_key = "&cx=" + config['PSE_KEY']
extra_params = "&lr=lang_en&num=10&hl=lang_en"

# Define your query parameters and values
query_params = [
    {"query_param": "q", "param_value": "Hannah Corbin Controversy"},
]

for params in query_params:
    query_param = params["query_param"]
    param_value = params["param_value"]

    result = make_api_call(base_url, api_key, pse_key, extra_params, query_param, param_value)
    ct = datetime.datetime.now()

    if result:
        directory = "/home/user/pse-script/results"
        filename = os.path.join(directory, f"api_result_{query_param}_{param_value}_{ct}.json")
        with open(filename, "w") as f:
            json.dump(result, f, indent=4)