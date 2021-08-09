class Employee:
	name=""
	age=0
	gender=""
	level=""
	
	def __init__(self, name, age, gender, level):
		self.name = name
		self.age = age
		self.gender = gender
		self.level = level


a = Employee("오상식",42,"남","차장")
b = Employee("천광웅",35,"남","과장")
c = Employee("장그래",28,"남","사원")
d = Employee("안영이",27,"여","사원")

employees = [a,b,c,d]
something = 0

print(len(employees))
for i in range(len(employees)):
		if(employees[i].gender == "남"):
			something = something + 1
print(something)
something = 0
for i in range(len(employees)):
	if(employees[i].age >= 40):
		something = something + 1
print(something)

Salary  = {
	"부장":700,
	"차장":600,
	"과장":500,
	"대리":400,
	"사원":300
}


something = 0
for i in range(len(employees)):
	something = something + Salary[employees[i].level]

print(something)
