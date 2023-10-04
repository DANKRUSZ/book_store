from lib.book_repository import BookRepository
from lib.book import Book


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/book_store.sql") 
    repository = BookRepository(db_connection) 

    books = repository.all() # Get all books

    # Assert on the results
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
    ]


def test_get_single_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    book = repository.find(3)
    assert book == Book(3, "Emma", "Jane Austen")


def test_create_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    repository.create(Book(None, "The Hobbit", "J.R.R. Tolkein"))

    result = repository.all()
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
        Book(6, "The Hobbit", "J.R.R. Tolkein")
    ]


def test_delete_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
    ]
    