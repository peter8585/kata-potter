class Potter:

    BOOKS = {'B1':1.0,'B2':2.0,'B3':3.0,'B4':4.0,'B5':5.0}

    PRICE = 8.0

    DISCOUNT = {5:10.0, 4:6.4, 3:2.4, 2:0.8, 1:0}

    def __init__(self):
        self.booksadded = {}

    def __init__(self, books):
        self.booksadded = books

    def addBook(self, book, price):
        pass

    def getPrice(self, book):
        total_price = 0.0

        if type(book) == float:
            if book in self.BOOKS.values():
                total_price = self.PRICE
        elif type(book) == list:
            total_price = len(book) * self.PRICE
        else:
            print('ERR')

        return total_price