import requests
import json
import os
import errno
import datetime

path = '/tmp/json_files/'
now = datetime.datetime.now()
filename = 'jsonT_' + str(now.strftime("%Y-%m-%d_%H:%M:%S"))


def check_exist_folder(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


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


@status_page
def get_json_response(response, state):
    p = []
    json_page = []
    check_exist_folder(os.path.join(path, filename + '.json'))

    with open(os.path.join(path, filename + '.json'), 'w', newline='\n') as f:
        json.dump(response.json(), f, indent=2)

    with open(os.path.join(path, filename + '.json')) as f:
        json_page = json.load(f)

    for i in json_page:
        if state is None:
            p.append({"num": i["number"], "link": i["html_url"], "title": i["title"]})
        if json_page[0]["state"] == state:
            p.append({"num": i["number"], "link": i["html_url"], "title": i["title"]})
        else:
            for k in i["labels"]:
                if k.get("name") == state:
                    p.append({"num": i["number"], "link": i["html_url"], "title": i["title"]})
    return p


def get_pulls(state):
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            auth=('', ''))
    return get_json_response(response, state)
