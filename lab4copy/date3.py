from datetime import datetime, timedelta

def drop_microseconds(date_mic):
    return date_mic.strftime("%Y-%m-%d %H-%M-%S")


current_datetime = datetime.now()
formatted_datetime = drop_microseconds(current_datetime)
print("Formatted datetime without microseconds:", formatted_datetime)
