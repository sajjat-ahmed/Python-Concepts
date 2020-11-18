import calendar

print(calendar.weekheader(5))

print(calendar.firstweekday())

print(calendar.month(2020,12))

print(calendar.monthcalendar(2020,6))

print(calendar.calendar(3000))

is_leapyear = calendar.isleap(2020)
print(is_leapyear)

how_many_leap_days = calendar.leapdays(2000, 2020)
print(how_many_leap_days)
