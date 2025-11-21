import calendar
year=int(input("enter a year: "))
if calendar.isleap(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
