import datetime

#datetime(year,month,date,hour(24),minute,second,microsecond)
x = datetime.datetime.today()
#y = datetime.datetime(2019-11-20 20:16:00)
print(x)

# y = datetime.datetime(2019-11-20 20:16:00)
y = datetime.datetime(2019, 11, 21, 20, 16, 00, 0, None)
print(y)

z = datetime.date.today()
q = datetime.time(20,12,20)

hasil = ""
hasil = hasil + z.__str__()
print(hasil)

f = " today"
ep = ("today" ==  f)
print(ep)
