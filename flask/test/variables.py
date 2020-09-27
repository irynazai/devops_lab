import requests
import re
from handlers.pulls import filename

# Enter your github login and password here:
login = ''
passwd = ''

# Enter url for api request
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'

response_closed = requests.get(url,
                               params={'per_page': '100', 'state': 'closed'}, auth=(login, passwd))
response_open = requests.get(url,
                             params={'per_page': '100', 'state': 'open'}, auth=(login, passwd))
response = requests.get(url,
                        params={'per_page': '100', 'state': 'all'}, auth=(login, passwd))

regex = re.sub(r'json[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{2}:[0-9]{2}:[0-9]{2}', '\n', filename)

template_all = [
    {
        'num': 1,
        'link': '',
        'title': '',
        'state': ''
    }
]
template_open = [
    {
        'num': 1,
        'link': '',
        'title': '',
        'state': 'open'
    }
]
template_closed = [
    {
        'num': 1,
        'link': '',
        'title': '',
        'state': 'closed'
    }
]
template_accepted = [
    {
        'num': 1,
        'link': '',
        'title': '',
        'state': '',
        'labels': [
            {'name': 'accepted'}
        ]
    }
]
template_need_work = [
    {
        'num': 1,
        'link': '',
        'title': '',
        'state': '',
        'labels': [
            {'name': 'needs work'}
        ]
    }
]
