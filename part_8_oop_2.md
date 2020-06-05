# Object Oriented Programming (contd.)

## Magic Methods
Set of methods that are automatically attached to all classes. There are a bunch of them. These are helpful in increasing
usability as well as for debugging purposes. They start and end with double underscores.
```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} costs {self.price}"

    def __repr__(self):
        return f"title={self.title}, price={self.price}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Book cannot be compared with another object that is not book")
        return self.title == other.title and self.price == other.price

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Book cannot be compared with another object that is not book")
        return self.price >= other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Book cannot be compared with another object that is not book")
        return self.price < other.price

b1 = Book("Title 1", 39.95)
b2 = Book("Title 1", 39.95)
b3 = Book("Title 2", 40.95)
print(b1)  # Title 1 costs 39.95
print(str(b1))  # Title 1 costs 39.95
print(repr(b1))  # title=Title 1, price=39.95
print(b1 == b2)  # True
print(b1 == b3)  # False
print(b1 >= b3)  # False
b4 = Book("Title 4", 10.9)
books = [b1, b2, b3, b4]
books.sort()
print([i.title for i in books])  # ['Title 4', 'Title 1', 'Title 1', 'Title 2']
print(b1 < 40)  # ValueError: Book cannot be compared with another object that is not book
```
`__str__` is used to represent the object as a string. `__repr__` is used to show the representation of the object as it is.
By default, objects do not know how to compare with each other. It cannot be perform attribute by attribute comparison.
The `__eq__` function is called when equality is checked on objects. Similarly, `__ge__` is called for checking greater than
or equality. `.sort()` function makes use of less than comparison. Hence, if a class has `__lt__` implementation, sort can
also be performed on a list of objects.
Additional magic method names can be found [here](https://docs.python.org/3/reference/datamodel.html#special-method-names)

```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self._discount = 0.1

    def __getattribute__(self, item):
        if item == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key == "price" and type(value) is not float:
            raise ValueError("The price attr must be a float")
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return item + " is not here!"

b1 = Book("Title 1", 39.95)
print(b1.price)  # 35.95
b1.price = 40.0
print(b1.price)  # 36.0
print(b1.hola)  # hola is not here
```
`__getattribute__` is called every time a class attribute is assessed. If you plan to override this function, do not use
`object_name.attr_name` to access attribute values. This will result in an indefinitely called `getattribute` function. Always
use `super().__getattribute__("attribute_name")`. Similar logic goes in `__setattr__` function. There is one more getter
function, `__getattr__`. This is called when `__getattribute__` lookup fails. i.e. it fails, throws exception, or attribute 
does not exist. Hence, it can be used to create attributes on the fly. But, be careful.

The object can be called as a function using `__call__` function.
```python
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} costs {self.price}"

    def __call__(self, title, price):
        self.title = title
        self.price = price

b1 = Book("Title 1", 39.95)
print(b1)  # Title 1 costs 39.95
b1("Anna Karenina", 49.95)
print(b1)  # Anna Karenina costs 49.95
```
The function can take any number of arguments. And can perform any function. In the example, the function is re-initializing
the attributes.

## Data Class
Supported in Python 3.7 and above. It is used to initialize attributes automatically in the `__init__` function. Data class
can be written by using `dataclasses` standard module. Add `@dataclass` annotation above the class definition. Though Python
is flexible about datatypes, the attributes types have to mentioned for the data class to work. However, the datatypes are 
not forced. Apart from the ease of writing concise code, data classes also implement `__repr__` and `__eq__` functions. 
It has all other features of a regular class. You can mention default values for attributes as well. However, attributes 
with no default value should be mentioned first followed by attributes with default values.  
There is another way of defining default values, i.e. by importing `field` from `dataclasses`. In this function, takes two 
arguments. If you set `default`, it will take the default value. If you use `default_factory`, you can calculate the default 
value using a function. 
```python
import random
from dataclasses import dataclass, field

def page_func():
    return random.randrange(20, 40)

@dataclass
class Book:
    title: str
    author: str = "No Author"
    price: float = field(default=0.0)
    pages: int = field(default_factory=page_func)

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}"

    def book_info(self):
        return f"{self.title} is written by {self.author}"

b1 = Book("Title 1", "ABC", 39.95)
b2 = Book("Anna Karenina", "Leo Tolstoy", 49.95)
b3 = Book("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)  # Book(title='Title 1', author='ABC', price=39.95, pages=29)
print(b1 == b2)  # False
print(b2 == b3)  # True
print(b2.book_info())  # Anna Karenina is written by Leo Tolstoy
print(b2.description)  # Anna Karenina by Leo Tolstoy
```
For additional initializations, you can override `__post_init__`. This is implicitly called after dataclass's `__init__`
function. It is useful when additional calculation/assignments are to be done based on other attributes.

To make certain attributes immutable, dataclasses provides `frozen` attribute. This does not allow methods as well, to 
modifying data.
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    title: str
    author: str = "No Author"
    price: float = 0.0

    def modifyPrice(self, new_price):
        self.price = new_price

b1 = Book("Title 1", "ABC", 39.95)
# b1.price = 15 # dataclasses.FrozenInstanceError: cannot assign to field 'price'
b1.modifyPrice(15)  # dataclasses.FrozenInstanceError: cannot assign to field 'price'
```
  
[Index](/README.md)