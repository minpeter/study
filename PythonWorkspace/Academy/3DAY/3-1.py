import math

class Circle:
	radius = 0
	diameter = 0
	circumference = 0
	area = 0
	
	def __init__(self, radius):
		self.diameter = radius * 2
		self.circumference = self.diameter * math.pi
		self.area = radius * radius * math.pi
		print("원의 원주 %d 원의 넓이 %d"%(self.circumference,self.area))

aaa = Circle(3)
