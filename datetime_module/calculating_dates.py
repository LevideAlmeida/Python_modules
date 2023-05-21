from datetime import datetime, timedelta

format_ = '%d/%m/%Y %H:%M:%S'
date1 = datetime.strptime('09/08/2023 14:17:10', format_)
date2 = datetime.strptime('05/07/2023 05:20:12', format_)


# getting difference between dates 
delta = date1 - date2
print(delta)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

print()

# Getting time count
delta = timedelta(days=12)
print(date1 + delta)

print()

# comparing dates
print(date1 > date2)
print(date1 < date2)
print(date1 == date2)
