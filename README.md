# Book API

A RESTful API built with Python and Flask for managing a collection of books.

The API allows users to retrieve, add, update, delete, and search for books. Book data is stored in a SQLite database.

## Features

* Get all books
* Get a single book by ID
* Add a new book
* Update an existing book
* Delete a book
* Search books by author
* Search books by publication year
* JSON responses
* SQLite database
* HTTP status codes for successful requests and errors

## Technologies Used

* Python
* Flask
* SQLite
* REST API
* JSON

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SammyDev19/book-api.git
```

2. Navigate into the project:

```bash
cd book-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the Flask development server:

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Get all books

```http
GET /books
```

Returns all books in the database.

### Get a single book

```http
GET /books/<book_id>
```

Example:

```text
GET /books/1
```

### Add a book

```http
POST /books
```

Request body:

```json
{
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
}
```

### Update a book

```http
PUT /books/<book_id>
```

Example:

```text
PUT /books/1
```

Request body:

```json
{
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
}
```

### Delete a book

```http
DELETE /books/<book_id>
```

Example:

```text
DELETE /books/1
```

### Search books

```http
GET /books/search
```

Search by author:

```text
/books/search?author=Tolkien
```

Search by year:

```text
/books/search?year=1937
```

You can also combine both:

```text
/books/search?author=Tolkien&year=1937
```

## HTTP Status Codes

| Status Code | Meaning                   |
| ----------- | ------------------------- |
| 200         | Request successful        |
| 201         | Book created successfully |
| 400         | Invalid request           |
| 404         | Book not found            |

## Project Structure

```text
book-api/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
├── README.md
```

The `books.db` file is generated locally and is excluded from Git using `.gitignore`.

## Author

Samuel Ogbolu
