import pytest
from ..potter import Potter

@pytest.fixture()
def potter():
    books = {}
    potter = Potter(books)
    return potter

def test_canAddBook(potter):
    potter.addBook(potter.BOOKS["BOOK1"],8)
    