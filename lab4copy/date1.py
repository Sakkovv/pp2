from datetime import datetime, timedelta

now_date = datetime.now()
result_date = now_date - timedelta(days=5)

formatted_result = result_date.strftime("%Y-%m-%d %H:%M:%S")

print("Результат после вычитания пяти дней:", formatted_result)



from datetime import datetime, timedelta

n = datetime.now()
r = now_date - timedelta()

f = r.strftime("%Y-%m-%d %H:%M:%S")
print(f)