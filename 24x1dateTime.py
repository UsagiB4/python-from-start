from datetime import *

# :::::::: Formatting Date times ::::::::::
"""
%d = shows date                 ||  %m = shows month number      ||  %H = hour (24)  ||  %S = second
%b = first 3 letters of Month   ||  %y = last 2 digit of a year  ||  %I = hour (12)  ||  %Z = time zone name (empty of naive)
%B = full month name            ||  %Y = full year               ||  %M = minute     ||  %c = shows complete time
%x = shows date dd/mm/yyyy      ||  %X = shows time hh:mm:ss     ||  %p = AM / PM    ||
"""
myDate = datetime.today()  # gives you date and time together
myDateShort = date.today()  # give only the date
print(myDate)
print(myDateShort)

newDate = myDate.strftime('%c')
print(newDate)
newDate = myDateShort.strftime('%c')
print(newDate)

myBDay = date(1987, 2, 5)
print(myBDay.strftime('%d/ %b/ %y'))
