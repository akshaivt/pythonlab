import time
import datetime
now=datetime.datetime.now()
print("current date and time: ",now)
print("current year:",now.year)
print("month of year:",now.strftime("%B"))
print("week number of the year: ",now.strftime("%U"))
print("weekday of the week: ",now.strftime("%A"))
print("day of year:",now.strftime("%j"))
print("day of month:",now.day)
print("day of week: ",now.strftime("%A"))
