
def search_book_by_name(name, collection):
    """Searches for a book by name in the collection and returns it as a dictionary"""
    # TODO: implement this function

def get_book_index(book, collection):
    """Returns the index of the given book in the collection."""
    # TODO: implement this function

def add_book(new_book, collection):
    """Check if the ISBN of the book is unique and then add it to the colllection."""
    # TODO: implement this function

def remove_book(book_name, collection):
    for book in collection:
        if book["title"] == book_name:
            collection.remove(book)
            return True
    return False

def borrow_book(book):
    """Decrese the number of available books by one. If already zero it raises an error."""
    available_count = int(book.get("available", 0))
    if available_count > 0:
        book["available"] = available_count - 1
        return True
    else:
        return False

def return_book(book):
    """Increase the bumber of available books by one. If the total number is exceeded this should be increased too."""
    # TODO: implement this function

def filter_for_available_books(collection):
    """Returns a new list with only books which are available."""
    available_books = []
    for book in collection:
        if int(book["available"]) > 0:
            available_books.append(book)
    return available_books

def filter_for_borrowed_books(collection):
    """Returns a new list with all books where at least one is not available."""
    borrowed_books = []
    for book in collection:
        if int(book.get("total")) != int(book["available"]):
            borrowed_books.append(book)
    return borrowed_books