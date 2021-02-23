'''Write a probram with a mother class Animal.
Inside it define a constructor with name and age parameters,
and say() method that returns the name and age of Anumal.
Then create two sub-classes Zebra and Dolphin.
Create two objects and call say method.
say method must be implemented only in Animal class.
(Hint, use class variable)'''


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"Hi, I am {self.__class__.__name__} {self.name} and I am {self.age}"


class Zebra(Animal):
    pass


class Dolphin(Animal):
    pass


d = Dolphin("Chuck", 20)
z = Zebra("Zelda", 30)

print(d.say())  # -> Hi, I am Dolphin Chuck and I am 20!
print(z.say())  # -> Hi, I am Zebra Zelda and I am 30!
