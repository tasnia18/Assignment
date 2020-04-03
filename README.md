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
python app.py

### Open Postman
#### For adding new books informantion send POST request on
http://localhost:5000/book?user=tasnia&password=hlw123              [here 'tasnia' is admin and 'hlw123' is password]
#### For update a book's informantion send PUT request on
http://localhost:5000/book/id?user=tasnia&password=hlw123         [here id is book's id no. which will be updated and it's a integer value]
#### For delete a book's informantion send DELETE request  
http://localhost:5000/book/id?user=tasnia&password=hlw123         [here id is book's id no. which will be deleted and it's a integer value]
#### For searching all books informantion send GET request on
http://localhost:5000/book                                          [Both admin and customer can search by request it]
#### For searching a book's informantion send GET request on
http://localhost:5000/book/id                                     [Both admin and customer can search by request it and here id is book's id no]
