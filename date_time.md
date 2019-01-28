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
### Time Delta
This module is used to perform date and time calculations. 
```Python
from datetime import date 
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1)) # 365 days, 5:01:00
today  = datetime.now()
print(today + timedelta(days=60)) # 2019-03-29 18:41:46.720811
print(today - timedelta(days=57)) # 2018-12-02 18:42:36.774421
```
**timedelta** object takes the following parameters: days, seconds, microseconds, milliseconds, minutes, hours, weeks. 
To find past or future dates, simply use plus or minus sign with the required difference from current date.
