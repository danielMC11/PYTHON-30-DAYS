from datetime import datetime, date, time, timedelta

rightnow = datetime.now()
print(rightnow)  # 2023-03-14 19:37:24.065237
year = rightnow.year
month = rightnow.month
day = rightnow.day
hour = rightnow.hour
minute = rightnow.minute
second = rightnow.second
print(f'{year}/{month}/{day} {hour}:{minute}:{second}')

full_time = rightnow.strftime('%Y/%m/%d %H:%M:%S Today is: %A')
print(full_time)

str_date = 'Today is Tuesday of 14 March 2023'
print(datetime.strptime(str_date, 'Today is %A of %d %B %Y'))

d = date(2003, 11, 19)  # date
print('My Date ', d)
print(f'Today of date object: {d.today()}, year {d.today().year}, month {d.today().month}, day {d.today().day}')

a = time()      # time
print("a =", a)
b = time(10, 30, 50)  # time(hour, minute and second)
print("b =", b)
c = time(hour=10, minute=30, second=50)
print("c =", c)
d = time(10, 30, 50, 200555)  # time(hour, minute, second, microsecond)
print("d =", d)

print('Date Time left for new year: ', date(year=2024, month=1, day=1) - date.today()) # output n days, h:m:s
print('Datetime Time left for new year: ', datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0, microsecond=0) - datetime.now())

#timedelta
t1 = timedelta(weeks=4, days=1, hours=2, minutes=24)
t2 = timedelta(weeks=2, days=2, hours=3, minutes=2)
print(t1 - t2)

print('Current day: ', datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
print('String to time: ', datetime.strptime('Today is 5 December, 2019', "Today is %d %B, %Y"))
print('Time Stamp: ', datetime.now().timestamp())
print(type(datetime.now()))