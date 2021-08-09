def solution(sirtSize):
	print(sirtSize)
	xs=s=m=l=xl=xxl = 0
	for i in range(len(sirtSize)):
		if 'XS' in sirtSize[i]:
			xs = xs + 1
		elif 'S' in sirtSize[i]:
			s = s + 1
	print(s)
	print(xs)
shirt_size = ['XS','XS','S','XS']
solution(shirt_size)

