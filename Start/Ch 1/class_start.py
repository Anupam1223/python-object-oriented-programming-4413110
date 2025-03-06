# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"hii this is me {self.title}"

# TODO: access the class attribute


# TODO: Create some book instances
book1 = Book("Brave new world")
book2 = Book("War and Peace")


# TODO: Use the static method to access a singleton object
book1.set_title("Brave")
print(book1)