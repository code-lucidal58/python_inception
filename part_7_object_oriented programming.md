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
 It defines a way to inherit attributes from one or many base classes. This can be used to reduce duplications. For example,
 a base class named `Publication` with title and price attributes, can be inherited by classes Magazine, Newspaper, and Book.
 ```python
class Publication:
    def __init__(self, title, price):
        self.tittle = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class Book(Publication):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author


class Newspaper(Periodical):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price, publisher, period)


class Magazine(Periodical):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price, publisher, period)
```
`Abstract Class` are templates for the inheriting class to follow. They have methods that child class has to implement.
Basically, they are used to enforce class constraints. One more constraint is that user will not be allowed to create an
object of the abstract class. All this constraints are followed by using `abc` standard module. 
```python
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

class Square(GraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calcArea(self):
        return self.side ** 2

c = Circle(10)
print(c.calcArea())  # 314
s = Square(10)
print(s.calcArea())  # 100
g = GraphicShape()  # TypeError: Can't instantiate abstract class GraphicShape with abstract methods calcArea
```
Python allows multiple inheritance, by mentioning the class names in the parentheses, separated by comma. This type of 
inheritance should be used carefully.
```python
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"

class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo) # foo
        print(self.bar) # bar
        print(self.name) # class A

c = C()
c.showprops()
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```
All classes, be it base or child, should implement `super().__init()`. Method Resolution Order (MRO) is a way in which complier
searches for attributes. It always searches the current class first. Then the parent classes in the order they are mentioned
inside parentheses. You can see the MRO using the function `__mro__` called on class.

Multiple Inheritance is important while creating interfaces.

## Interfaces
 