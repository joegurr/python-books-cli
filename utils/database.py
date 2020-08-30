import json

FILENAME = '/Users/josephgurr/Development/python-books-cli/utils/books.json'

books = []

def clear():
    global books
    books = []
    with open(FILENAME, 'w') as file:
        json.dump({}, file)


def add_book(book):
    global books
    books.append(book)
    with open(FILENAME, 'w') as file:
        json.dump({'books': books}, file)
    get_books()

def get_books():
    global books
    with open(FILENAME, 'r') as file:
        books = json.load(file)['books']
    return books


def read_book(name):
    global books
    for book in books:
        if book['name'] == name:
            book['read'] = True

            with open(FILENAME, 'w') as file:
                json.dump({'books': books}, file)

            get_books()
            break
    else:
        print(f'{name} is not in your list')


def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)

            with open(FILENAME, 'w') as file:
                json.dump({'books': books}, file)

            get_books()

            break
    else:
        print(f'{name} is not in your list')

