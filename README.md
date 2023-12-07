
# Case Course Watch
The website will have the ability to notify CWRU students when previously full courses on SIS have open seats. By using our service, students will have an easier time getting into courses they want, leading to a less stressful course registration process.

# Set Up 

Please use terminal to run frontend and backend to open our application for proper usage.

## Backend Setup
First, run our backend to have system set up. Please enter the following in terminal. 

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 backend/app.py
```

Then, connect to the database server using a database connection tool like SQL Tools or a Postgre Driver. If you don't have a database connection tool, download SQLTools or download Postgre Connecter. 

Using this connection tool, select connection using connection string and use the input below to connect to database. 
Also, name your connection to whatever name you want it.  

```
postgres://swe_project_user:Hm9jhHzZa5WDHOWQbDTPIiGHHLNScvb3@dpg-cln4iqkjtl8s7397h5n0-a.ohio-postgres.render.com/swe_project?ssl=true

```

Click connect now and your connection to the database is established. 

## Frontend Dev Setup
Then, to open application on your local device on chrome, please enter the following to open and the application is ready to use!!

``` 
cd CCW-Frontend 
npm install
npm run dev
```

Application is ready to use. 

# Application Instructions 

Please use the sign up feature to register with our application. To access your account, use the login in feature. 

Once logged in, click add class and once window with class form pops up, fill in class that you would like to be notified off. 
Then, the class should be added to the table of tracked classes and you will have options to update that list. 

Once class spot open, the application will give you a notification that course has a spot ready to be enrolled in. 

Click add course and start class search to see if a class in open.

# Running Tests

## Frontend Tests

Run frontend first, then run testcases

```
cd CCW-Frontend
npm run cypress:open
```

Then choose Chrome browser and run all testcases.

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

