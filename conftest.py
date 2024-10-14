import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def book_name():
    book_name = 'Гордость и предубеждение и зомби'
    return book_name

@pytest.fixture
def collector_add_book(collector, book_name):
    collector.add_new_book(book_name)
    return collector
