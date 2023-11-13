
# Case Course Watch
This is a web app that notifies users when their classes become available on SIS. 

# Set Up 

## Frontend Dev Setup

``` 
cd CCW-Frontend 
npm install
npm run dev
```

## Backend Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install requirements.txt
```

# Running Tests

# Frontend Tests

Run frontend first, then run testcases
cd CCW-Frontend
npm run cypress:open

Then chose Chrome browser and run all testcases.

This was done on my mac and hopefully you have your dependencies installed . . . which I didnt keep track of. Hopefully npm install does all the dependencies stuff for you 

## Backend Tests

To run a specific tests:

```
cd backend/tests
python3 <test_name>.py
```

To check code coverage for a specific test:

```
cd backend/tests
coverage run -m unittest <test_name>.py
```

You can view the code coverage results in two ways:

1. Printed to the console

```
coverage report -m
```

2. As an HTML file (open the generated htmlcov/index.html in your browser)

```
coverage html
```