# This program is to calculate the next April fool's day
from datetime import date 
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today()
afd = date(today.year, 4, 1) # Feed AFD

if afd < today:
    print("April Fool's day already went by %d days ago" % (today-afd).days)
    afd = afd.replace(year = today.year+1)
time_to_afd = afd - today # this create time.delta
print("It's just", time_to_afd.days, "days until April fool's day")
