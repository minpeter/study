import datetime

time = datetime.datetime.now()

nowh = int(time.strftime("%H"))
nowm = int(time.strftime("%M"))

endh = 19
endm = 45
h = endh-nowh
m = 0

if(nowm<=endm):
	m = endm-nowm
elif(nowm>=endm):
	h = h - 1
	endm = endm+60
	m = endm-nowm


print("%d시간%d분 남았습니다"%(h,m))
