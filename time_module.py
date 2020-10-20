import time

# # Wall clock time ---------------------------------------------------------------->
# print('The time is:', time.time())  #---------->not human redable

# print('The time is:', time.ctime()) #---------->human redable

# # Monotonic clock------------------------------------------------------------------>
# print(time.monotonic())

# # Sleep clock----------------------------------------------------------------------->
# time.sleep(5)
# print("Hello sir")

# # Whole information of local time --------------------------------------------------->
# print(time.localtime())

import datetime

# # Set a time-------------------------------------------------------------------------->
# t  = datetime.time(9,42,30,0)
# print(t)

# # print(datetime.time.min)
# # print(datetime.time.max)
# # print(datetime.time.resolution)

# # Shows the date of today------------------------------------------------------------->
# print(datetime.date.today())

# a = datetime.date.today()
# print(a.ctime())

# print(a.timetuple())

# # Set a date------------------------------------------------------------------------->
# print(datetime.date(2020,10,20))

# b = datetime.date(2020,10,20)
# c = b.replace(year=2030)
# print(c.ctime())

# # Set whole data---------------------------------------------------------------------> 
# print(datetime.datetime(2020,10,20,10,4,30,0))

# # Shows whole data------------------------------------------------------------------>
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# print(datetime.datetime.utcnow())