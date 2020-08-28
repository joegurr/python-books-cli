from utils import database

USER_CHOICE = """
Please enter one of the following:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
"""

SIMPLE_USER_CHOICE = "\n(a)dd, (l)ist, (r)ead, (d)elete, (q)uit\n"

def get_book_name():
    return input('What is the name of the book: ')


def get_book_info():
    name = get_book_name()
    author = input('Who is the author: ')
    read = input('Have you read this book (y/n): ')
    # could check for valid input here?
    if read != 'y' or read != 'Y':
        read = False
    else:
        read = True

    return { 'name': name, 'author': author, 'read': read }


def add_book():
    book = get_book_info()
    database.add_book(book)


def list_books(): 
    books = database.get_books()

    for book in books:
        book_string = f'{book["name"]} was written by {book["author"]}. '
        if book['read']:
            book_string = book_string + 'I have finished it.'
        else:
            book_string = book_string + 'I have not read it yet.'
        
        print(book_string)

def read_book():
    name = get_book_name()
    database.read_book(name)


def delete_book():
    name = get_book_name()
    database.delete_book(name)


USER_OPTIONS = {
    'a': add_book,
    'l': list_books,
    'r': read_book,
    'd': delete_book,
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in USER_OPTIONS:
            USER_OPTIONS[user_input]()
        else:
            print('Unknown command, please try again')
        
        user_input = input(SIMPLE_USER_CHOICE)

    print('Thanks, bye')

menu()
