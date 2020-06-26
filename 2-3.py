file = open("버킷리스트.txt","w")
bucketlist = []

def addlist():
	bucketlist.append(input("하고 싶은 일을 입력:"))

def savelist():
	file.write(str(bucketlist))
	

for i in range(5):
	addlist()
savelist()


file.close()


