import datetime

time = datetime.datetime.now()

nowh = int(time.strftime("%H"))
nowm = int(time.strftime("%M"))

print(nowh,nowm)

classh = 20
classm = 10

print("%d시간%d분 남았습니다"%(classh-nowh,classm-nowm))
