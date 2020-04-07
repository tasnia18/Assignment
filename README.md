## Library website 

 Ensure you have the following on your PC:

- Python 3
- Pipenv
- Virtualenv (or virtualenvwrapper)
- Docker Desktop

### Install Python Modules

$ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy

$ pipenv install pylint-flask 

### Activate venv

$ pipenv shell

### Create DB by writing those on command

$ python

>> from app import db

>> db.create_all()

>> exit()

### Run Server

>python app.py

#### Library.rar is the Flask application without Docker

### Documentation using Postman
https://documenter.getpostman.com/view/10932897/SzYbxxCX?version=latest

### Containerize the solution with Docker

> Create "Dockerfile" on the project

> We have to specify the host as 0.0.0.0 in "app.py" file

> We can then build our image with the docker build command :

>> docker build . -t doc-flask:v1

> Once the build process is done, we can run the application with the docker run command :

>> docker run -p 5000:5000 doc-flask:v1
