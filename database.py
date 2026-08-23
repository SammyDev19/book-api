import os
import sqlite3


class Database:

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "books.db")

        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        """)

        self.connection.commit()

    def get_books(self):
        self.cursor.execute("""
            SELECT * FROM books
        """)

        return self.cursor.fetchall()

    def add_book(self, title, author, year):
        self.cursor.execute("""
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
        """, (title, author, year))

        self.connection.commit()
        return self.cursor.lastrowid

    def get_book(self, book_id):
        self.cursor.execute("""
            SELECT * FROM books
            WHERE id = ?
        """, (book_id,))

        return self.cursor.fetchone()

    def update_book(self, book_id, title, author, year):
        self.cursor.execute("""
            UPDATE books
            SET title = ?, author = ?, year = ?
            WHERE id = ?
        """, (title, author, year, book_id))

        self.connection.commit()
        return self.cursor.rowcount

    def delete_book(self, book_id):

        self.cursor.execute("""
            DELETE FROM books
            WHERE id = ?
        """, (book_id,))

        self.connection.commit()
        return self.cursor.rowcount

    def search_books(self, author=None, year=None):
        query = "SELECT * FROM books WHERE 1=1"
        params = []

        if author:
            query += " AND author LIKE ?"
            params.append(f"%{author}%")

        if year:
            query += " AND year = ?"
            params.append(year)

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        return [
            {
                "id": row[0],
                "title": row[1],
                "author": row[2],
                "year": row[3]
            }
            for row in rows
        ]