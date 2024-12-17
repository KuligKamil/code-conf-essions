# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/#object-attribute-lookup


class Test:
    pass


print(a := Test())
print("isinstance ", isinstance(a, Test))
print("a is Test ", a is Test)
print(a.__class__)
print(a.__dict__)


# inheritance.py


class Parent:
    speaks = ["English"]

    def __init__(self):
        self.listens = ["English"]


class Child(Parent):
    def __init__(self):
        super().__init__()  # without this line, listens will be not exist
        self.speaks.append("German")
        self.listens.append("German")
        self.listens.append("Spanish")


print(a := Child())
print(a.speaks)
print(a.listens)


def get_representations(obj):
    return (repr(obj), str(obj))


import datetime

today = datetime.datetime.now()

a = get_representations(today)
print(a)


# class Car:

#     def __init__(self, color, mileage) -> None:
#         self.color = color
#         self.mileage = mileage

#     def __str__(self) -> str:
#         return f"The {self.color} car has {self.mileage:,} miles."


# my_car = Car("blue", 20000)
# print(my_car)
# my_car = Car("red", 30000)
# print(my_car)


# dog.py


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


# Create a GoldenRetriever class that inherits from the Dog class.
# Give the sound argument of GoldenRetriever.speak() a default value of "Bark".


salary_sigma_programmer = 1_000_000
print(f"{salary_sigma_programmer:,}")
print(f"{salary_sigma_programmer:_}")
# "{0:,.2f}".format(1234567.89)
print(f"{1234567.89:,.2f}")


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

# setter only works when the property is set, not in initialization
c = Circle(-1)
c.radius = -2

# In Python, how can you add function-like behavior to a public attribute without breaking the API?


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()


#For example, if you use the data class infrastructure 
# to write a custom class, then you won’t have to implement 
# special methods like 
#.__init__(), .__repr__(), .__eq__(), and .__hash__(). 
# The data class will write them for you.
        
sequence protocol vs iterable protocol

# https://realpython.com/python-data-classes/


https://www.youtube.com/watch?v=d3F-C472cqQ
# when use static class when classmethod
# https://realpython.com/instance-class-and-static-methods-demystified/
