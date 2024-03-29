from utils.database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection("data.db") as connection:
        connection.cursor().execute(
            "CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)"
        )


def add_book(book):
    name = book["name"]
    author = book["author"]
    read = book["read"]

    with DatabaseConnection("data.db") as connection:
        connection.cursor().execute(
            "INSERT INTO books VALUES(?, ?, ?)", (name, author, read)
        )


def get_books():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = [
            {"name": row[0], "author": row[1], "read": row[2]}
            for row in cursor.fetchall()
        ]

    return books


def read_book(name):
    with DatabaseConnection("data.db") as connection:
        connection.cursor().execute("UPDATE books SET read=1 WHERE name=?", (name,))


def delete_book(name):
    with DatabaseConnection("data.db") as connection:
        connection.cursor().execute("DELETE FROM books WHERE name=?", (name,))
