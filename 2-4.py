class Brawler:
	name = ""
	health = 0
	attack = 0

	def introduce():
		print("안녕 나는 %s이고 체력은 %d, 공격력은 %d이야"%(Brawler.name,Brawler.health,Brawler.attack)

	def __init__(self, name, health, attack):
		self.name = "shelly"
		self.health = 3600
		self.attack = 1500
		self.introduce()


