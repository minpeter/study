import datetime
t = ['월', '화', '수', '목', '금', '토', '일']
today = datetime.datetime.now()
print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 {t[today.weekday()]}요일 입니다.")
