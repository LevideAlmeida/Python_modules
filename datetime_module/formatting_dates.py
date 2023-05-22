from datetime import datetime


# date = datetime(2022, 12, 16, 15, 6, 19)
date = datetime.strptime('2022-12-13 15:06:19', '%Y-%m-%d %H:%M:%S')
print(date.strftime('%d/%m/%Y'))

date_now = datetime.now()
print(date_now)
print(date_now.strftime('%d/%m/%Y %H:%M'))
print(date_now.strftime('%d/%m/%Y %H:%M:%S'))
print(date_now.strftime('%d/%m/%y'))