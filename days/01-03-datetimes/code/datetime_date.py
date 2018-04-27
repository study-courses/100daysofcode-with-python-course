#!python3

from datetime import datetime
from datetime import date

print(datetime.today())
# datetime.datetime(2018, 2, 19, 14, 38, 52, 133483)

today = datetime.today()

print(type(today))
# <class 'datetime.datetime'>

today_date = date.today()

print(today_date)
# datetime.date(2018, 2, 19)

print(type(today_date))
# <class 'datetime.date'>

print(today_date.month)
# 2

print(today_date.year)
# 2018

print(today_date.day)
# 19

christmas = date(2018, 12, 25)
print(christmas)
# datetime.date(2018, 12, 25)

if christmas is not today_date:
    print("Sorry there are still " + str((christmas - today_date).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
