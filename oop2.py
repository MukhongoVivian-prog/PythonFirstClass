def movement():
    print("person is walking")


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


a = Person("joe", 23, "male")
print(a.name)
b = Person("mary", 24, "female")
print(b.name)
c = Person("jane" ,21, "female" )
print(c.name)