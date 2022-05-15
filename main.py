from .potter import Potter

books = [1,1,2,2,3,3,4,5]

print(type(books))
potterer = Potter(books)

print(potterer.getPrice(books))