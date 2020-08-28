books = []

def add_book(book):
    books.append(book)


def get_books():
    for book in books:
        book_string = f'{book["name"]} was written by {book["author"]}. '
        if book['read']:
            book_string = book_string + 'I have finished it.'
        else:
            book_string = book_string + 'I have not read it yet.'
        
        print(book_string)

def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            break
    else:
        print(f'{name} is not in your list')


def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)
            break
    else:
        print(f'{name} is not in your list')
