
# Case Course Watch
The website will have the ability to notify CWRU students when previously full courses on SIS have open seats. By using our service, students will have an easier time getting into courses they want, leading to a less stressful course registration process.

# Set Up 

Please use terminal to run frontend and backend to open our application for proper usage.

## Backend Setup
First, run our backend to have system set up. Please enter the following in terminal. 

```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


## Frontend Dev Setup
Then, to open application on your local device on chrome, please enter the following to open and the application is ready to use!!

``` 
cd CCW-Frontend 
npm install
npm run dev
```


Application is ready to use. 

## Application Instructions 

Please use the sign up feature to register with our application. To access your account, use the login in feature. 

Once logged in, click add class and once window with class form pops up, fill in class that you would like to be notified off. 
Then, the class should be added to the table of tracked classes and you will have options to update that list. 

Once class spot open, the application will give you a notification that course has a spot ready to be enrolled in. 



