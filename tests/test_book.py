from lib.book import Book

def test_constructs_with_fields():
    book = Book(1, "Nineteen Eighty Four", "George Orwell")
    assert book.id == 1
    assert book.title == "Nineteen Eighty Four"
    assert book.author == "George Orwell"

def test_equality():
    book_1 = Book(1, "Nineteen Eighty Four", "George Orwell")
    book_2 = Book(1, "Nineteen Eighty Four", "George Orwell")
    assert book_1 == book_2

def test_formatting():
    book = Book(1, "Nineteen Eighty Four", "George Orwell")
    assert str(book) == "Book(1, Nineteen Eighty Four, George Orwell)"