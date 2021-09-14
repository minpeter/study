from datetime import datetime

today = datetime.now()
day = datetime(2021, 12, 31, 0, 0, 0)

print("현재 날짜: ",today.strftime("%Y-%m-%d"))
print("방학식까지 남은 날:", day-today)