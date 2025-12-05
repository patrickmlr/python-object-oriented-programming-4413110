# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __book_list = None

    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def get_book_list():
        if Book.__book_list is None:
            Book.__book_list = []
        return Book.__book_list

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types: ", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title2", "PAPERBACK")

# TODO: Use the static method to access a singleton object
the_books = Book.get_book_list()
the_books.append(b1)
the_books.append(b2)
print(the_books)