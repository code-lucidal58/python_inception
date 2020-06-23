# Loops and Conditionals
Python supports **for, while, if-elif-else** blocks.

## If-elif-else
The concept of if-else block is similar to any other language.
```Python
x = 10
if x>10:
  print("x is greater than 10")
elif x < 10:
  print("x is less than 10")
else:
  print("x is equal to 10")

print("x is less than 10" if x<10 else "x is greater than equal to 10") # not good handle block statements
```
***NOTE***: Python does not support switch statement.

## While
While loop continues execution till the condition given in true. If the condition involves variable, it must be updated 
in each loop statement execution. Otherwise it may result in infinite loop. This execution style is used when the number 
of times the statement block is to be executed is unknown.
```Python
x = 10
while x>=0:
  print(x)
  x-=1
```
Python does not have `do-while` loop. However, it can be implemented by using `while True:` i.e. an infinite loop, and mention
the condition for breaking, in the end of the code block.
An `else` block can also be added to `while`. The `else` block statements will execute when the `while` loop execution 
completes smoothly i.e. is not stopped by a `break`. 
***NOTE*** Python supports `break` and `continue` like any other high level language.  
**PS**: A `continue` or `break` inside a `try-except-finally` block inside a loop, will still always execute the `finally` block.
```python
a = 0
b = 2
while a < 3:
    a += 1
    b -= 1
    try:
        a / b
    except ZeroDivisionError:
        print("division by zero")
        break
    finally:
        print("finally executed")
"""OUTPUT
finally executed
division by zero
finally executed
"""
```

## For loop
This is mainly used to iterate through iterables i.e. list, dictionary, set, etc.
```Python
d = {"a":1,"b":2,"c":3}
for i in d: # i is the iterator
  print(i, d[i])
'''
a 1
b 2
c 3
'''
arr = [3,2,6]
for item in arr:
  print(item, end=' ')
# 3 2 6
for i, value in enumerate(arr):
  print(i , value)
'''
0 3
1 2
2 6
'''
```
`enumerate()` returns index and value in form a tuple.  
`range()` is used to traverse through pre-defined sequences like integers. Atleast one argument is required. 
`range(10)` : returns a list wth numbers from 0 to 9.  
`range(1,10)` : returns a list wth numbers from 1 to 9.  
`range(1,10, 2)` : returns a list wth numbers from 1 to 9, with step size 2 i.e. [1,3,5,7,9]  
This can be traversed in `for` loop as follows: 
```python
for i in range(1, 101):
  print(i**2)
```
This will print square of all numbers from 1 to 100.  
`else` can be added to the end of `for` loop, executed when `for` is NOT stopped by `break`, i.e. if `for` loop had smooth 
execution till end of condition.

[Next](./date_time.md)  
[Index](/README.md)
