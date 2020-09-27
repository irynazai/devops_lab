### **A simple web application with tests that allows you to receive pull requests from a github.**

#### Description:
*Using this script you can launch a web application and request pull requests from the github repository.. You can choose between "open" and "closed" pull requests, or pull requests marked with a label "accepted" or "need work".*
*The app has 83% unit test coverage.*

#### Requirements:
*Please add your credentials such as "login" and "passwd" in "./flask/handlers/pulls.py" and in "./flask/test/test_pulls.py" if you need.*
*Attention: if you exceed the number of requests from one IP, then access to receiving pull requests will not be available.*


*You need to install next packages. Run command:*
- pip install Jinja2
- pip install flask
- pip install requests
- pip install unittest2

#### How to use. Run command:
- python flask/start.py

#### How to start unittests. Run command:
- python flask/test/test_pulls.py

### Or

#### You can use nose and coverage packages. Install it:
- pip install nose
- pip install coverage

And start tests by:
- nosetests --with-coverage --cover-package=handlers/ --cover-erase 

