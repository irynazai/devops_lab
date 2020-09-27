import requests
import json
import os
import errno
import datetime

# Enter your github login and password here:
login = ''
passwd = ''

# Enter url for api request
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'

# Enter directory for saving json files
path = '/tmp/json_files/'
now = datetime.datetime.now()
filename = 'json' + str(now.strftime("%Y-%m-%d_%H:%M:%S"))


def check_exist_folder(my_path):
    if not os.path.exists(os.path.dirname(my_path)):
        try:
            os.makedirs(os.path.dirname(my_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    return os.path.exists(os.path.dirname(my_path))


def status_page(func):
    def wrapper(response, state):
        if response.status_code == 200:
            print('Success!')
        if response.status_code == 500:
            print('Internal Server Error.')
        if response.status_code == 502:
            print('Bad Gateway.')
        if response.status_code == 503:
            print('Service Unavailable.')
        if response.status_code == 504:
            print('Gateway Timeout.')
        if response.status_code == 401:
            print('Unauthorized Error.')
        if response.status_code == 403:
            print('Forbidden.')
        elif response.status_code == 404:
            print('Not Found.')
        return func(response, state)
    return wrapper


def create_json_file(response):
    check_exist_folder(path)
    with open(os.path.join(path, filename + '.json'), 'w', newline='\n') as f:
        json.dump(response.json(), f, indent=2)
    return f.name


def load_from_json_to_list():
    with open(os.path.join(path, filename + '.json')) as f:
        json_page = json.load(f)
    return json_page


@status_page
def get_json_response(response, state):
    p = []
    create_json_file(response)
    json_page = load_from_json_to_list()
    for i in json_page:
        if state is None:
            if json_page[0]["state"] == 'open' or json_page[0]["state"] == 'closed':
                t = {"num": i["number"], "link": i["html_url"], "title": i["title"], "state": json_page[0]["state"]}
                p.append(t)
        elif json_page[0]["state"] == state:
            t = {"num": i["number"], "link": i["html_url"], "title": i["title"], "state": str(json_page[0]["state"])}
            p.append(t)
        else:
            for k in i["labels"]:
                if k.get("name") == state:
                    t = {"num": i["number"], "link": i["html_url"], "title": i["title"], "labels": [{"name": state}]}
                    p.append(t)
    return p


def get_pulls(state):
    if state == 'open' or state == 'closed':
        response = requests.get(url, params={'per_page': '100', 'state': state}, auth=(login, passwd))
    else:
        response = requests.get(url, params={'per_page': '100', 'state': 'all'}, auth=(login, passwd))
    return get_json_response(response, state)
