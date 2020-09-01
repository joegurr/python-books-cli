import sqlite3


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()

def add_book(book):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    name = book['name']
    author = book['author']
    read = book['read']

    cursor.execute('INSERT INTO books VALUES(?, ?, ?)', (name, author, read))

    connection.commit()
    connection.close()


def get_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()

    return books


def read_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
 
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()


