import datetime
import calendar

now = datetime.datetime.now()
yr = int(31556926)

if calendar.isleap(now.year):
    leap_year = True
else:
    leap_year = False
nowyear = now.year

while True:
    age = int(input("how old are you "))

    now = nowyear * yr

    age = age * yr

    now = now - age

    now = now / yr

    ni = int(now)
    print("you were born on =", ni)
