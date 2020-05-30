# Object Oriented Programming (OOP) with Python

## Terms related to OOP
* Class: A blueprint of creating objects of a particular type
* Methods: Regular functions that are part of a class
* Attributes: Variables that hold data that are part of a class
* Object: a specific instance of a class
* Inheritance: means by which a class can inherit capabilities from another
* Composition: Means of building complex objects out of other objects

## Classes - Basics
`class` keyword is used to create a new class. Parentheses after class name is required only when you are inheriting 
another class. The built-in initialization function is `__init__`. It can be overridden. This function is the 
first one to be called when the object is created. To repeat, this function is implicitly called after object is created.
Therefore, it will not be appropriate to call it the constructor. Rather, it is the initializing function, for initializing 
attributes. 
All methods have their first attribute as the object itself. This parameter is by convention called `self`. Of course,
there are exceptions to the first parameter being the object itself.
```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.__secret = "Hello there!"
        
    def get_price(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price*self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount

b = Book("War and Peace", 39.95)
print(b.title) #The monk who solved his ferrari
print(b.get_price())
b.set_discount(0.25)
print(b.price)
print(b.__secret)
print(b._Book_secret)
print(type(b))
print(isinstance(b, Book))
print(isinstance(b, object))
```
Here `title` is called the `instance attribute`, because the value to this attribute is unique for each instance. Similarly, 
`instance methods` will have their first parameter as the object as `self`. In the `set_discount` method, a new instance
variable is created `_discount`. The underscore(_) in the variable name indicates that this attribute should not be called 
outside the class. This attribute is for internal purpose only. In the function `get_price`, the function `hasattr` is used
to check if the object has the instance attribute `_discount`. The instance atrribute `__secret` has a double underscore. 
Compiler prevents usage of this attribute outside the class by internally changing the attribute name. That is called name
mangling. Compiler adds the class name in front of the such attributes. 

There are two ways of check the type of an object. One way is using the built-in `type` function and checking the output string,
or using `isinstance` function. This function checks for parent class as well. That is why, `isinstance(b, object)` return true,
because all classes in Python inherit `object` class. 

```python
class Book:
    book_types = ("hard cover", "paper back", "ebook")
    
    @classmethod
    def get_book_types(cls):
        return cls.book_types

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.book_types:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.book_type = booktype

print(Book.get_book_types())
b1 = Book("Title1", "hard cover")
b2 = Book("Title2", "comic")
```
`book_type` is a class attribute. It is not unique to an instance. Any change made to this attribute will be adopted by all objects,
even by the one already created. Similarly, `get_book_types` is a class method. They work on class. That is why, there is atleast one
parameter to such method, that is the class itself. 

```python
class Book:

    __bookList = None
    @staticmethod
    def getbooklist():
        if Book.__bookList is None :
            Book.bookList = []
        return Book.__bookList
    def __init__(self, title, booktype):
        self.title = title
        self.book_type = booktype

b1 = Book("Title 1", "hard")
b2 = Book("Title 2", "soft")
# use the static method to access a singleton object
books = Book.getbooklist()
books.append(b1)
books.append(b2)
print(books)
```
Static methods are global functions in the class namespace. It is used when a singleton object is created for the class, like in this
case, the attribute `__bookList`. There are not many great usages of static methods.

## Inheritance
 