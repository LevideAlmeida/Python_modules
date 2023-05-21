from datetime import datetime
from pytz import timezone

# datetime.now() => returns the current date and time
date_now = datetime.now()
print(date_now)
date_now = datetime.now()
print(date_now)


# about timezones:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

date_now_in_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(date_now_in_tokyo)


# Timestamps:
# https://pt.wikipedia.org/wiki/Era_Unix

print(date_now.timestamp())
print(datetime.fromtimestamp(127182719))