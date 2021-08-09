file = open('애국가.txt','r')
lines = file.readlines()
j = 0

print(file)
for i in range(len(lines)):
	if lines[i] == '\n':
		j = j + 1
		print(j)
	else:
		print(lines[i])

file.close()
