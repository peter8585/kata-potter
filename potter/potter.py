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

    def getDiscount(self, count):
        return self.DISCOUNT[count]

    def getDiscountedPrice(self, books):
        totalPrice = 0.0
        if books is None:
            books = self.booksadded
        if (len(books) == len(set(books))):
            return (len(books) * self.PRICE) - self.getDiscount(len(books))
        else:
            arrangedSetList = self.getArrangedSets(books)
            return self.getDiscountedPriceForList(arrangedSetList)

    def getArrangedSets(self, books):
        arrangedSetList = []
        for item in books:
            if len(arrangedSetList) == 0 :
                arrangedSetList.append([item])
            else:
                self.updatedArrangedList(item, arrangedSetList)
        return arrangedSetList

    def updatedArrangedList(self, item, arrangedSetList):
        itemArranged = False
        discountDict = {}
        for setitem in arrangedSetList:
            if not (item in setitem):
                setitem.append(item)
                discountDict[self.getDiscountedPriceForList(arrangedSetList)] = setitem
                setitem.remove(item)
                itemArranged = True
        if itemArranged :
            minval = min(discountDict.keys())
            setItem = discountDict.get(minval)
            setItem.append(item)

        if not itemArranged:
            arrangedSetList.append([item])
        return  arrangedSetList

    def getDiscountedPriceForList(self,arrangedSetList):
        totalPrice = 0.0
        for setItem in arrangedSetList:
            totalPrice = totalPrice + self.getDiscountedPrice(setItem)
        if totalPrice <= 0.0:
            return len(books) * self.PRICE
        else:
            return totalPrice