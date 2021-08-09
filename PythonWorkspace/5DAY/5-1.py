import datetime

time = datetime.datetime.now()

nowh = int(time.strftime("%H"))
nowm = int(time.strftime("%M"))

endh = int(input("끝나는 시간을 입력하세요:"))
endm = int(input("끝나는 분을 입력하세요:"))
h = endh-nowh
m = 0

if(nowm<=endm):
	m = endm-nowm
elif(nowm>=endm):
	h = h - 1
	endm = endm+60
	m = endm-nowm


print("%d시간%d분 남았습니다"%(h,m))
