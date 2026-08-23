from flask import Flask, jsonify, request
from database import Database


app = Flask(__name__)

database = Database()


# Home route to confirm that the API is running.
@app.route("/")
def home():
    return jsonify({
        "message": "Book API is running"
    })


# Get all books.
@app.route("/books", methods=["GET"])
def get_books():

    books = database.get_books()

    books_list = []

    for book in books:

        books_list.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "year": book[3]
        })

    return jsonify(books_list)


# Add a new book.
@app.route("/books", methods=["POST"])
def add_book():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    title = data.get("title")
    author = data.get("author")
    year = data.get("year")

    if not title or not author or year is None:
        return jsonify({
            "error": "title, author and year are required"
        }), 400

    database.add_book(title, author, year)

    return jsonify({
        "message": "Book added successfully"
    }), 201


# Get a single book by its ID.
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):

    book = database.get_book(book_id)

    if not book:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify({
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "year": book[3]
    })


# Update an existing book by its ID.
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    title = data.get("title")
    author = data.get("author")
    year = data.get("year")

    if not title or not author or year is None:
        return jsonify({
            "error": "title, author and year are required"
        }), 400

    updated = database.update_book(
        book_id,
        title,
        author,
        year
    )

    if updated == 0:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify({
        "message": "Book updated successfully"
    })


# Delete a book by its ID.
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):

    deleted = database.delete_book(book_id)

    if deleted == 0:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify({
        "message": "Book deleted successfully"
    })


# Search books by author or year.
@app.route("/books/search")
def search_books():

    author = request.args.get("author")
    year = request.args.get("year")

    books = database.search_books(author, year)

    return jsonify(books)


# Start the Flask development server.
if __name__ == "__main__":
    app.run(debug=True)