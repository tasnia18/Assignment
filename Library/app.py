from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Book Class/Model
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  bookTitle = db.Column(db.String(100), unique=True)
  author = db.Column(db.String(100))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, bookTitle, author, price, qty):
    self.bookTitle = bookTitle
    self.author = author
    self.price = price
    self.qty = qty

# Book Schema
class BookSchema(ma.Schema):
  class Meta:
    fields = ('id', 'bookTitle', 'author', 'price', 'qty')

# Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Add a Book
@app.route('/book', methods=['POST'])
def add_book():
  user = request.args.get('user')
  password = request.args.get('password')

  if user=='tasnia' and password=='hlw123':
    bookTitle = request.json['bookTitle']
    author = request.json['author']
    price = request.json['price']
    qty = request.json['qty']

    new_book = Book(bookTitle, author, price, qty)

    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book)
  else:
    return 'Username or password is incorrect'
# Get All Books
@app.route('/book', methods=['GET'])
def get_books():
  all_books = Book.query.all()
  result = books_schema.dump(all_books)
  return jsonify(result)


# Get Single Book
@app.route('/book/<id>', methods=['GET'])

def get_book(id):
 # bookTitle=request.args.get('bookname')
  book = Book.query.get(id)
  return book_schema.jsonify(book)

# Delete a Book
@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
  user = request.args.get('user')
  password = request.args.get('password')

  if user =='tasnia' and password=='hlw123':
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)
  else:
    return 'Username or password is incorrect'
# Update a Book
@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
  user = request.args.get('user')
  password = request.args.get('password')
  if user=='tasnia' and password=='hlw123':
    book = Book.query.get(id)
    bookTitle = request.json['bookTitle']
    author = request.json['author']
    price = request.json['price']
    qty = request.json['qty']
    book.bookTitle = bookTitle
    book.author = author
    book.price = price
    book.qty = qty
    db.session.commit()
    print('Book information updated')
    return book_schema.jsonify(book)
  else:
    return 'Username or password is incorrect'
# Run Server
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)