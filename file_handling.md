## File Handling
Python provides built in functions to work with file. No import is required.
```python
f = open("textfile.txt", "w+")
for i in range(10):
    f.write("This is line"+str(i)+"\n")
f.close()
```
```open``` function takes two arguments. One is the file name, and the other is the mode in which you want 
to open the file. Here it is **w+** meaning - open file in write mode, create file if it does not exist. 
Similarly **r** and **a** stands for read and append mode respectively. ```f.read()``` is used to read the 
entire content of the file. While, ```f.readline()``` reads line by line and returns a list.

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
print("Item path:", path.realpath("textfile.txt"))
print("Item path and name:", path.split(path.realpath("textfile.txt"))) # returns a tuple
```
```os.path``` modules provides access to all features of a file. This includes modification time, creation time, etc. 
```python
import time
t = time.ctime(path.getmtime("textfile.txt")) # 'Tue Jan 29 12:14:03 2019'
print(datetime.datetime.getTimeStamp(path.getmtime("textfile.txt"))) # 2019-01-29 12:14:03.159570
```
```.getmtime``` return the modified time in float. ```time.ctime``` is used to convert it to real time.
Following are examples to copying, renaming a file., and archiving the entire folder or specific files in the folder.
```python
import shutil
import os
from os import path
from shutil import make_archive
from zipfile import ZipFile
shutil.copy(src, dest) # copy file from src to destination
# destination should contain file name as well
os.rename("old_name", "new_name")
# To zip a folder
root_dir, tail = path.split(src)
make_archive(archive_name, "zip", root_dir)
# When selective file is to added to zip
with ZipFile("textarchive.zip", "w") as newzip:
    newzip.write("textfile.txt")
    newzip.write("textfile.txt.bak")
```

[Next](web_data_handling.md)  
[Index](/README.md)