import pickle
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def __str__(self):
        return f"{self.name} is {self.age} years old"

f = open("person_data.bin", "wb")

p = Person("John", 30)

pickle.dump(p, f)

f.close()

f = open("person_data.bin", "rb")
person = pickle.load(f)
print(person)

f.close()