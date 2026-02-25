from datetime import datetime, timedelta
x = datetime.now()
variable = x - timedelta(days=5)
print(variable)
#2
yesterday = x - timedelta(days=1)
print(yesterday)

tomorrow = x + timedelta(days=1)
print(tomorrow)
#3
without_microseconds = x.replace(microsecond=0)
print(without_microseconds)
#4
date1 = datetime(2026, 2, 26, 10, 0, 0)
date2 = datetime(2026, 2, 25, 8, 30, 0)

difference = date1 - date2

seconds = difference.total_seconds()

print("Difference in seconds:", seconds)