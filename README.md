## **A simple web application that allows you to receive pull requests from a github.**

## Description:
*Using this script you can launch a web application and request pull requests from the github repository.. You can choose between "open" and "closed" pull requests, or pull requests marked with a label "accepted" or "need work".*

# Requirements:
*Please add your credentials in "./flask/handlers/pulls.py" file in function get_pulls(): auth=('your_github_user_name', 'your_github_password'))*
*If you exceed the number of requests from one IP, then access to receiving pull requests will not be available.*


*You need to install next packages. Run command:*
- pip install Jinja2
- pip install flask
- pip install requests

# How to use. Run command:
- python flask/start.py


