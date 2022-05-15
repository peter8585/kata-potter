import pytest
from ..potter.potter import Potter

@pytest.fixture()
def potter():
    books = {}
    potter = Potter(books)
    return potter

def test_canAddBook(potter):
    potter.addBook(potter.BOOKS["BOOK1"],8)
    

def test_basicsPrice(potter):
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK1"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK2"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK3"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK4"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK5"])
  assert 8.0 * 3 == potter.getPrice([potter.BOOKS["BOOK5"], potter.BOOKS["BOOK4"],potter.BOOKS["BOOK3"]])


def test_getDiscountItems(potter):
    assert 10.0 == potter.getDiscount(5)
    assert 6.4 == potter.getDiscount(4)
    assert 2.4 == potter.getDiscount(3)
    assert 0.8 == potter.getDiscount(2)
    assert 0 == potter.getDiscount(1)



def test_simpleDiscounts(potter):
  assert 8 * 2 * 0.95 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK2"]])
  assert 8 * 3 * 0.9 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK3"] ,potter.BOOKS["BOOK5"]])
  assert 8 * 4 * 0.8 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"],potter.BOOKS["BOOK2"],potter.BOOKS["BOOK3"],potter.BOOKS["BOOK5"]])
  assert 8 * 5 * 0.75 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK2"], potter.BOOKS["BOOK3"], potter.BOOKS["BOOK4"], \
                                                    potter.BOOKS["BOOK5"]])


def test_severalDiscounts(potter):
  assert 8 + (8 * 2 * 0.95) == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"],potter.BOOKS["BOOK2"]])
  assert 2 * (8 * 2 * 0.95) == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"],potter.BOOKS["BOOK2"],potter.BOOKS["BOOK2"]])
  assert (8 * 4 * 0.8) + (8 * 2 * 0.95) == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"],potter.BOOKS["BOOK2"],\
                                                                      potter.BOOKS["BOOK3"],potter.BOOKS["BOOK3"],potter.BOOKS["BOOK4"]])
  assert 8 + (8 * 5 * 0.75) == potter.getDiscountedPrice( [potter.BOOKS["BOOK1"], potter.BOOKS["BOOK2"], potter.BOOKS["BOOK2"], potter.BOOKS["BOOK3"], \
                                                           potter.BOOKS["BOOK4"], potter.BOOKS["BOOK5"]])



def test_edgeCasesDiscounts(potter):
  assert 2 * (8 * 4 * 0.8) == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"],potter.BOOKS["BOOK2"], potter.BOOKS["BOOK2"],\
                                                         potter.BOOKS["BOOK3"],potter.BOOKS["BOOK3"],potter.BOOKS["BOOK4"],potter.BOOKS["BOOK5"]])

  assert 3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8) == potter.getDiscountedPrice(\
      [potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"], potter.BOOKS["BOOK1"],potter.BOOKS["BOOK1"], \
       potter.BOOKS["BOOK2"], potter.BOOKS["BOOK2"], potter.BOOKS["BOOK2"], potter.BOOKS["BOOK2"],potter.BOOKS["BOOK2"], \
       potter.BOOKS["BOOK3"], potter.BOOKS["BOOK3"], potter.BOOKS["BOOK3"], potter.BOOKS["BOOK3"], \
       potter.BOOKS["BOOK4"], potter.BOOKS["BOOK4"], potter.BOOKS["BOOK4"], potter.BOOKS["BOOK4"],potter.BOOKS["BOOK4"], \
       potter.BOOKS["BOOK5"], potter.BOOKS["BOOK5"], potter.BOOKS["BOOK5"], potter.BOOKS["BOOK5"]])