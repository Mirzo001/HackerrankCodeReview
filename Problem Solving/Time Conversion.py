from datetime import *

s = '12:01:00PM'
x = '12:01:00AM'


def timeConversion(s):
    s = datetime.strptime(s, "%I:%M:%S%p")
    new_time = datetime.strftime(s, "%H:%M:%S")
    print(new_time) 

timeConversion('12:01:00AM')
