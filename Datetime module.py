#----------------------------Date and Time----------------------------------------------
# Following modules are used to work with date,time,and duration.
#1.time
#2.datetime

# Epoch-The epoch is the point where the time starts and is platform dependent.
# This point is taken as the january 1st of the current year 00:00:00.For Unix, the
# epoch is january 1st 1970.

# UTC-UTC is coordinated universal Time (formerly known as greenwich mean ,Time,or GMT).
# The acronym UTC is not mistake but a compromise between English and French.

#                               Time Module
# time() Function-This function return the time in seconds since the epoch as a floating
# point number.The specific date of the epoch and the handling of leap seconds is
# platform dependent.

# ctime() Function-This function is used to get current date and time.When we pass epoch
# time in seconds to the function, it returns corresponding date and time in string format.
# when we do not pass epoch time,it returns current date and time in string format.

# localtime() Function-This function is used to convert second into date and time.it returns
# an object struct_time which can be used to access the attributes either using an index or using
# a name.

# tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst,tm_zone,Tm_gmtoff..

#Example:-1
from time import time,ctime,localtime
t=time()
print(t)

ct=ctime()
print(ct)

l=localtime()
print(l)

#Example:-2
from time import time,ctime,localtime

l=localtime()
print("year:",l.tm_year)
print("Months:",l.tm_mon)
print("Date:",l.tm_mday)
print("Hours:",l.tm_hour)
print("Minutes:",l.tm_min)
print("Seconds:",l.tm_sec)

l=localtime()
print(l.tm_mday,end='/')
print(l.tm_mon,end='/')
print(l.tm_year)

l=localtime()
print(l.tm_hour,end='/')
print(l.tm_min,end='/')
print(l.tm_sec)

#--------------------------------datetime module----------------------------------------
# datetime:-It handles date and time.It has year,month,day,hour,minute,seconds,microsecond
# and tzinfo attributes.

# date:-It handles dates of gregorian calender,without taking time zone into consideration.
# It has year,month and day attributes.

# time:-It handles time assuming that every day has exactly 24*60*60 seconds.It has hour    ,
# minutes,seconds,microsecond and tzinfo attributes.

# timedelta:-It handles duration .This duration may be the difference between two date,
# time or datetime instances.

# Example:-1
from datetime import datetime

dt1=datetime(year=2025,month=8,day=24)
dt2=datetime(year=2025,month=8,day=24,hour=22,minute=12)
dt3=datetime(2025,8,24)
dt4=datetime(2025,8,24,22,12)
print(dt1)
print(dt2)
print(dt3)
print(dt4)

#Example:-2
dt2=datetime(year=2025,month=8,day=24,hour=22,minute=12)
print(dt2.year)

#                              datetime class methods
# now():-This method is used to get the current date and time.We can provide timezone
# information to this method.If the timezone is not provided.then it takes the local time
# zone. it returns an object that contains date and time information in my timezone.We
# can use day,month,year, hour,minute and seconds.

#Ex:-datetime.now()

# today():-This method is used to get the current date and time.it returns the date and
# time information.

#Ex:-datetime.today()

from datetime import datetime

ct=datetime.now()
print(ct)
print(ct.day)
print(ct.year)

ct=datetime.today()
print(ct)
print(ct.hour)

#----------------------------------------time class-------------------------------------
from datetime import time

t=time(hour=22, minute=28, second=45)
print(t)
print(t.hour)

#-----------------------------------------timedelta class-------------------------------
from datetime import timedelta,date

td=timedelta(days=10)
d=date.today()
print(d+td)
print(d-td)

#--------------------------compare two dates--------------------------------------------
from datetime import date

d1=date(2019,6,30)
d2=date(2010,6,30)

print(d1==d2)
print(d1>d2)
print(d1<d2)
print(d1!=d2)

