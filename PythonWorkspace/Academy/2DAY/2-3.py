file = open("버킷리스트.txt","w")
bucketlist = []

def addlist():
	bucketlist.append(input("하고 싶은 일을 입력:"))

def savelist():
	for i in range(len(bucketlist)):
		file.write('%s\n'%str(bucketlist[i]))
	

for i in range(5):
	addlist()
savelist()


file.close()


