from datetime import *

# ::::: .time() :::::
# time(hour, min, sec, micro_sec,)
a = time(5, 10, 34, 1342)
print(a)
# time() is a small time module. it's limited upto micro_sec

# :::::: .datetime() ::::::
# datetime(year, month, day, hour, min, sec, micro_sec)
# datetime() gives you a wider range of time. from Year to micro_second.
b = datetime(1999, 2, 23, 12, 54, 32, 12342)
print(b)
presentTime = datetime.now()
print(presentTime.utcnow())  # show time relative to UTC

