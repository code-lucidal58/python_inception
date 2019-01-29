## File Handling
Python provides built in functions to work with file. No mport is required.
```python
f = open("textfile.txt", "w+")
for i in range(10):
    f.write("This is line"+str(i)+"\n")
f.close()
```
```open``` function takes two arguments. One is the file name, and the other is the mode in which you want to open the file. Here it is **w+** meaning - open file in write mode, create file if it does not exist. 
Similarly **r** and **a** stands for read and append mode respectively. ```f.read()``` is used to read the entire content of the file. While, ```f.readline()``` reads line by line and returns a list.

### Operating System related features
**os** module is used to perform operating system related operations. The **path** module in it is used for path related features.
```python
import os
from os import path
print(os.name)
print("Item exists: "+str(path.exists("textfile.txt")))
print("Item is a file: "+str(path.isfile("textfile.txt")))
print("Item is a directory: "+str(path.isdir("textfile.txt")))
print("Item path: "+str(path.realpath("textfile.txt")))
```