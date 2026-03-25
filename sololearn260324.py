# class Student:
#     def __init__(self, name):
#         self.name = name
#     def sayHi(self):
#         print("Hi from "+ self.name)

# s1= Student("John")
# s1.sayHi()

# class Rectangle:
#     def __intit__(self, width, height):
#         self.width = width
#         self.height = height
# rect = Rectangle(7, 8)
# print(rect.color)

# Inheritance
# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# class Cat(Animal):
#     def purr(self):
#         print("Purr...")

# class Dog(Animal):
#     def bark(self):
#         print("Woof!")

# fido = Dog("Fido", "brown")
# print(fido.name)
# fido.bark()

# subclass, Superclass

# class Wolf:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def bark(self):
#         print("Grr...")
# class Dog(Wolf):
#     def bark(self):
#         print("Woof!")

# huskey = Dog("Max", "grey")
# huskey.bark()

# class A:
#     def method(self):
#         print(1)

# class B(A):
#     def method(self):
#         print(2)

# B().method()

# class A:
#     def method(self):
#         print("A method")
# class B(A):
#     def another_method(self):
#         print("B method")
# class C(B):
#     def third_method(self):
#         print("C method")

# c = C()
# c.method()
# c.another_method()
# c.third_method()

# class A:
#     def a(self):
#         print(1)
# class B(A):
#     def a(self):
#         print(2)
# class C(B):
#     def c(self):
#         print(3)
# c=C()
# c.a()

# class A:
#     def spam(self):
#         print(1)
# class B(A):
#     def spam(self):
#         print(2)
#         super().spam()
# B().spam()

# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)

# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first + second
# print(result.x)
# print(result.y)

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         return "\n".join([self.cont, line, other.cont])

# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#     def __gt__(self, other):
#         for index in range(len(other.cont)+1):
#             result = other.cont[:index] + ">" + self.cont
#             result += ">" + other.cont[index:]
#             print(result)

# spam = SpecialString("spam")
# eggs = SpecialString("eggs")
# spam > eggs

# import random

# class Veguelist:
#     def __init__(self, cont):
#         self.cont =cont

#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1,1)]

#     def __len__(self):
#         return random.randint(0, len(self.cont)*2)

# vague_list = Veguelist(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])

# a=42
# b=a
# c=[a]
# del a
# b = 100
# c[0] = -1

# class Queue:
#     def __init__(self, contents):
#         self.__hiddenlist=list(contents)

#     def push(self, value):
#         self.__hiddenlist.insert(0, value)

#     def pop(self):
#         return self.__hiddenlist.pop(-1)

#     def __repr__(self):
#         return "Queue({})".format(self.__hiddenlist)

# queue = Queue([1, 2, 3])
# print(queue)
# queue.push(0)
# print(queue)
# queue.pop()
# print(queue)
# print(queue.__hiddenlist)

# class Spam:
#     __egg = 7
#     def print_egg(self):
#         print(self.__egg)

# s = Spam()
# s.print_egg()
# print(s._Spam__egg)
# print(s.__egg)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

#     @classmethod
#     def new_square(cls, side_length):
#         return cls(side_length, side_length)

# square = Rectangle.new_square(5)
# print(square.calculate_area())

# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#     @staticmethod
#     def validate_topping(topping):
#         if topping == "pineapple":
#             raise ValueError("No pineapples!")
#         else:
#             return True
# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)

# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#     @property
#     def pineapple_allowed(self):
#         return False
# pizza = Pizza(["cheese", "tomamto"])
# # print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True


# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#         self._pineapple_allowed = False

#     @property
#     def pineapple_allowed(self):
#         return self._pineapple_allowed

#     @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         if value:
#             password = input("Enter the password: ")
#             if password == "sw0rdfish!":
#                 self._pineapple_allowed = value
#             else:
#                 raise ValueError("Akert! Ubtruder!")


# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)


