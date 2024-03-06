from datetime import datetime, timedelta

user_input = input("")

if not user_input:
    user_date = datetime.now()
else:
    user_date = datetime.strptime(user_input, "%Y-%m-%d")

previous_day = user_date - timedelta(days=1)
next_day = user_date + timedelta(days=1)

print("Previous day:", previous_day.strftime("%Y-%m-%d"))
print("Input day:", user_date.strftime("%Y-%m-%d"))
print("Next day:", next_day.strftime("%Y-%m-%d"))
