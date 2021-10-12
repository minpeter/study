class Animal:
    def __init__(self, speices, age):
        self.speices = speices
        self.age = age
    
    def eat(self, food):
        print(f"{self.speices}이(가) {food}를(을) 먹는다")


class Pet(Animal):
    def __init__(self, name, speices, age):
        super().__init__(speices, age)
        self.name = name

class Dog(Pet):
    def __init__(self, name, speices, age):
        super().__init__(name, speices, age)

    def bark(self):
        print(f"🔊 {self.name}이(가) 왈왈 짖습니다.")

class Cat(Pet):
    def __init__(self, name, speices, age):
        super().__init__(name, speices, age)

    def bark(self):
        print(f"🔊 {self.name}이(가) 야옹 소리를 냅니다.")


dog = Dog("강아지이름","🐩", 12)
dog.bark()

cat = Cat("그린","🐈‍", 10)
cat.bark()