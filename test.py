import datetime
from dateutil.rrule import rrule, DAILY

a = datetime.datetime(2023, 4, 17)
b = datetime.datetime.now()

for dt in rrule(DAILY, dtstart=a, until=b):
    print(dt.strftime("%Y-%m-%d"))