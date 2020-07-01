file = open("db/박스오피스.txt",'r')

class Movie:
	title = ""
	country = ""
	director = ""
	audience = 0

	def __init__(self,title,country,director,audience):
#print("%s %s %s %s"%(title,country,director,audience))
		self.director = director
		



lines = file.readlines()
movielist = []


for i in range(len(lines)):
	x = (lines[i].split())
	j = Movie(x[0],x[1],x[2],x[3])
	movielist.append(j)


#print(movielist)	
print(movielist[1].director)
	



