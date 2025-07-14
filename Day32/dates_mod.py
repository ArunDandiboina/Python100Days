from datetime import datetime

now = datetime.now()
print(now)
print(now.day)
print(now.strftime("%A"))  # Full weekday name
print(now.strftime("%B"))  # Full month name
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Custom format


if (now.weekday() == 6):
    print("It's Sunday!")