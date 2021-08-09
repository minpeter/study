import random
lopeo = [] #list of people
lopen = [] #list of penalty
nop = int(input("게임할 사람 인원:")) #Number of people

for i in range(nop):
	lopeo.append(input("%d번째 사람이름 입력:"%(i+1)))

for i in range(nop):
	lopen.append(input("%d번째 벌칙 입력:"%(i+1)))

print('='*20)

for i in range(nop):	
	'''
	randomPeo = random.choice(lopeo)
	randomPen = random.choice(lopen)
	print("%s --> %s"%(randomPeo,randomPen))
	lopeo.remove(randomPeo)
	lopen.remove(randomPen)
	#print(lopeo,lopen)
	'''
	randomPen = random.choice(lopen)
	print("%s --> %s"%(lopeo[i],randomPen))
	lopen.remove(randomPen)
