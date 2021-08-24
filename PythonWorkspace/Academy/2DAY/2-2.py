file = open("치킨.txt","r")
lines = file.readlines()
menu = {}
something = 0

for i in range(len(lines)):
	x = lines[i].split()
	menu[x[0]] = x[1]
	
	something = something + int(x[1])
	
	
print(menu)
print(something)
