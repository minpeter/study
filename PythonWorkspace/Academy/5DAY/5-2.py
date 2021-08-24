import random
lop = [] #list of people
nop = int(input("게임할 사람 인원:")) #Number of people

for i in range(nop):
	lop.append(input("%d번째 사람이름 입력:"%(i+1)))

print("%s 당첨"%(random.choice(lop)))

