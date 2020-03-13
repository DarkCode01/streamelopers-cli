import os
import json
import requests


def parser_data(data_json):
    return json.dumps(data_json, indent=4)


def get_setttings_file_obs(url):
    print("Request to get obs settings...")
    response = requests.get(url)
    
    return response.json()

def make_settings_file_obs(data_json):
    if not os.path.isdir(f'{os.environ.get("HOME")}/.sdcli/'):
        print("Creating folder of sdcli settings...")
        os.mkdir(f'{os.environ.get("HOME")}/.sdcli/')

    with open(f'{os.environ.get("HOME")}/.sdcli/settings.obs.json', 'w') as settings_obs:
        print("Creating file of obs settings...")
        settings_obs.write(data_json)

def do_setup():
    SETTINGS_OBS = "https://gist.githubusercontent.com/DarkCode01/93f2cee3bdfcad8608b65075486e5486/raw/30f17cc7dd85583d351765c472720596c5d8e9b4/streamelopers.obs.json"

    make_settings_file_obs(parser_data(get_setttings_file_obs(SETTINGS_OBS)))

    print("configurated :D")
