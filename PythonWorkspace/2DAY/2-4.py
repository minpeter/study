class Brawler:
	name = ""
	health = 0
	attack = 0

	def introduce(self):
		print("안녕 나는 %s이고 체력은 %d, 공격력은 %d이야"%(self.name,self.health,self.attack))

	def __init__(self, name, health, attack):
		self.name = name
		self.health = health
		self.attack = attack
		self.introduce()

shelly = Brawler("쉘리", 3600, 1500)
bull = Brawler("불", 5030, 2333)
leon = Brawler("레온", 3333, 3333)


