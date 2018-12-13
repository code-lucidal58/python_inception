### List
Lists are similar to arrays. The following operations can be performed on a list.
```Python
l = []
l.insert(1,3) # (index, value)
l.append(8) #add to the end of list
l.remove(6) #removes the first instance of the data in the list
l.pop() # removes last element 
print(l) #prints list
l.sort() # sorts list in ascending order
l.reverse() #this does not change the origib]nal list. Used to reverse order of elements
```
Sorting a nested list based on say nth element of the list elements in list:
```l.sort(key = lambda x: x[3])``` where n is 3 here. Soring is done based on 4th element
To print a list, where each element is separated by a common sequence, **.join()** is used.
```python
l=[1,2,3,4]
print(" ".join(l)) # 1 2 3 4
```

### Map
The **map()** function applies a given function to each item of an iterable (list, tuple etc.) and returns a map object of the 
results. This result is then typecasted to list, set or any data type as required.
```python
def square(n):
  return n*n
numbers = [1, 5, 8, 14]
result = map(square, numbers)
print(result) # <map object at 0x7f722da129e8>
numbersSquare = set(result)
print(numbersSquare) # {1, 25, 64, 196}
# A single line substitute for the above code
print(set(map(lambda x: x*x, numbers)))
```
Passing multiple iterators to lambda function:
```python
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = list(map(lambda n1, n2: n1+n2, num1, num2))
```

### Strings
```.startwith``` and ```endswith``` are two methods that can be used with string to check the starting and ending substring 
respectively.
```python
s = "Hello There"
print(s.startwith("Hello")) # True
print(s.endwith("era")) # False
```
```.split()``` function is called on a string, returns a list, where elements are decided based on a delimiter.
```python
s="My name is Joker"
print(s.split(' ')) #['My', 'name', 'is','Joker']
print("12-08-2018".split('-')) # ["12","08","2018"]
```
```.strip()``` removes trailing whitespaces in the string.
```python
s = "    hello     "
print(s.strip()) #hello
```
