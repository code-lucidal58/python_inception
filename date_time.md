## Date and Time
Date time operations in Python is performed usinf *datetime* library in python. This is one of the inbuilt libraries of Python.
```Python
from datetime import date 
from datetime import time
from datetime import datetime

today = date.today()
print(today) # 2019-01-28
print(today.day, today.month, today.year) # 28 1 2019
print(today.weekday()) # 0

today = datetime.now()
print(today) # 2019-01-28 18:35:27.562771
t = datetime.time(datetime.now())
print(t) # 18:35:27.563741
```
```today.weekday()``` returns an integers in the range 0 to 6, where 0 represents Monday and 6 represents Sunday.

### Date and Time Formating
