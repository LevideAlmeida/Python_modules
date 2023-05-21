# Datetime module
# Module used to get date and times
# Create dates with datetime class
# datetime(year, month, day)
# datetime(year, mouth, day, hour, minute, second)

from datetime import datetime

date = datetime(2014, 10, 3)
date2 = datetime(2023, 5, 21, 15, 50, 20)
print(date)
print(date2)


# Create dates with strings
# datetime.strptime(date, date_format)
# the date format use directives like:
# %d => Day of the month as a zero-padded decimal number.
# %m => Month as a zero-padded decimal number.
# %Y => Year with century as a decimal number.
# All directives to format dates are in the documentation

str_date_date = '2006-08-09 14:35:10'
str_date_fmt =  '%Y-%m-%d %H:%M:%S' # Format of the string date

date3 = datetime.strptime(str_date_date, str_date_fmt)
print(date3)

# date in the brazilian format
str_date_date = '15/04/2009'
str_date_fmt = '%d/%m/%Y'

brazilian_date = datetime.strptime(str_date_date, str_date_fmt)
print(brazilian_date)

