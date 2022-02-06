from datetime import *
currentDate = date.today()  # time format >>> yyyy-mm-dd
#print(currentDate)
#print(currentDate.year)  # returns current year
#print(currentDate.day)  # returns current day


#____ change your current date____
currentDate = currentDate.replace(1999, 3, 30)
#print(currentDate)

#_____weekday_____
toDay = date.today()
wDay = toDay.weekday()  # in python days are numbered as Monday 0 - Sunday 6
print(wDay)
