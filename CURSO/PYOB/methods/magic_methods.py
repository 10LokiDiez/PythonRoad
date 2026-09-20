# Magic methods = Dunder methods __init__
#                 built-in operations
#                 Methods that are used for customize tehe bihavior of objects


class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self): #Este sirve para cuando imprimamos el objeto aparezca como nosotros queremos
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, item):
        return item in self.title or item in self.author
    
    def __getitem__ (self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self. num_pages
        else:
            return f"This {key} key was not found"
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Esmesmeris book", "Esmesmeris D' Garp", 174)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)

books = [book1, book2, book3]
for book in books:
    print(book)


print(book1 == book4)
print(book1 > book4)
print(book2 < book4)
print(book2 + book4)
print("Hobbit" in book1)

print(book3["author"])
print(book3["material"])