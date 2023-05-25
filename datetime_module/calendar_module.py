"""
Using calendar for calendars and dates
https://docs.python.org/3/library/calendar.html
calendar is used for generic calendars and dates stuff.
with calendar, you can get:
- What is the last day of the month (ex.: monthrange)
- What is the name and number of any day (ex.: weekday)
- Create calendar (ex.: monthcalendar)
By default, day of week start in 0 and end in 6
0 = Monday | 6 = Sunday
"""

import calendar

# print(calendar.calendar(2022)) # Print 2022 calendar
# print(calendar.month(2023, 5)) # Print 2023/05 calendar
# print(list(calendar.day_name)) # Print the list with the names of days

# Return a tuple with the first day of month and the last day of month
# print(calendar.monthrange(2023, 5))

number_of_first_day, last_day = calendar.monthrange(2023, 5)
print(calendar.day_name[number_of_first_day])
print(calendar.weekday(2023, 5, last_day)) # Print the weekday of 2023/05/last_day
