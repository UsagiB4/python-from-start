from datetime import *
currentDate = date.today()  # time format >>> yyyy-mm-dd
print(currentDate)
print(currentDate.year)  # returns current year
print(currentDate.day)  # returns current day


#____ change your current date____
currentDate = currentDate.replace(1999, 3, 30)
print(currentDate)
