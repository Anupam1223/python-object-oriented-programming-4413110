class Baap:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Book(Baap):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Baap):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Newspaper(Baap):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)     # Aldous Huxley
print(n1.publisher)  # New York Times Company
print(b1.price, m1.price, n1.price)  # 29.0 5.99 6.0
