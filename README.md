# Sample-python-rest

## Purpose

Question: What is the purpose of this project?

Answer: To understand how to use REST with Python
* Using Flask - it's a Python micro web framework that acts as a web server listening for REST requests

## Requirements
The relevant Flask Rest library needs to be installed for this API to work (run's in the background and listen for REST calls)
```
pip3 install flask-restful
```
You can use the default unittest framework that Python3 provides however to run the tests in pytests you will need to install it:
```
pip install pytests
```

## Instructions
From the root directory of the project, we firstly need to run the Flask web server:
```
python3 app.py
```
This should print out the following output. This indicates that the web server is listening for REST requests on ttp://127.0.0.1:5000/:
```
➜  sample-python-rest git:(master) python3 sample-python-rest/app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 630-421-997
```
### GET Hero
Perform a GET curl request to get a hero:
```
curl --request GET http://localhost:5000/Hero/Superman
```
The expected (or similar) output should be:
```
"Superman"
```
If the hero does not exist (e.g. /Hero/Robin/), you will get the following output:
```
"Robin not found"
```
### POST Hero
Perform a POST curl request to create a new hero:
```
curl --request POST http://localhost:5000/Hero/Joker
```
The expected (or similar) output should be:
```
"Joker has been added"
```
If you try to add it again, you will get the following output:
```
"Unable to add Joker as it already exists"
```

## Testing
This project contains two tests. A passing and a failing one.
Firstly, this project assumes that the application is already running. For that reason we first need to start the REST application:
```
python3 app.py
```
Once started, we can run all the tests using unittest:
```
python3 -m unittest discover
```
You should see an output similar to the below:
```
...
FAIL: test_hero_fails (test.test_hero.TestHero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mohammeduddin/Documents/GitProjects/msu/sample-python-rest/test/test_hero.py", line 12, in test_hero_fails
    assert request_json_body == 'Batman'
AssertionError

----------------------------------------------------------------------
Ran 2 tests in 0.020s

FAILED (failures=1)
...
```
You can also use pytest to run the tests:
```
pytest
```
This should give a more meaningful output:
```
...
test/test_hero.py .F                                                                                                           [100%]

============================================================== FAILURES ==============================================================
______________________________________________________ TestHero.test_hero_fails ______________________________________________________

self = <test.test_hero.TestHero testMethod=test_hero_fails>

    def test_hero_fails(self):
        request_json_body = requests.get('http://localhost:5000/Hero/Robin').json()
>       assert request_json_body == 'Batman'
E       AssertionError: assert 'Robin not found' == 'Batman'
E         - Robin not found
E         + Batman

test/test_hero.py:12: AssertionError
...
```

## Implementation Notes
* Parameter name in add_resource must match parameter name in Rest methods e.g.
```
App.py
...
api.add_resource(Hero, '/Hero/<string:get_name>')
...
```
```
Hero.py
...
def get(self, get_name):
...
```