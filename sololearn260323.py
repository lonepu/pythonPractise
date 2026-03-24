#from itertools import count
#for i in count(3):
#    print(i)
#   if i>=11:
#        break


#from itertools import accumulate, takewhile
#nums = list(accumulate(range(8)))
#print(nums)
#print(list(takewhile(lambda x: x<= 6, nums)))

#from itertools import product, permutations
#letters = ("A", "B", "C", "D")
#print(list(product(letters, range(2))))
#print(list(permutations(letters)))

#from itertools import product
#a={1,2}
#print(len(list(product(range(3),a))))

#nums={1,2,3,4,5,6}
#nums={0,1,2,3}&nums
#nums=filter(lambda x: x>1, nums)
#print(len(list(nums)))

# def power(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x*power(x,y-1)
# print(power(2,3))

# a = (lambda x: x*(x+1))(6)
# print(a)

# nums = [1,2,8,3,7]
# res=list(filter(lambda x: x%2==0, nums))
# print(res)

# a=[1,2,3,4,5]
# b=[3,4,5,6,7]
# print(set(a)-set(b))

# num = int(input())
# def fibonancci(n):
#     def get_fib(i):
#         if i <= 1:
#             return i
#         return get_fib(i-1) + get_fib(i-2)
#     for i in range(n):
#         print(get_fib(i))
# fibonancci(num)

# class Cat:
#     def __init__(self, color, legs):
#         self.color = color
#         self.legs = legs

# flix = Cat("ginger", 4)
# rover = Cat("dog-colored", 3)
# stumpy = Cat("brown", 3)

# print(flix.color)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def check_result(self):
#         if self.marks >= 50:
#             return f"{self.name} passed the exam."
#         else:
#             return f"{self.name} failed the exam."
        
# Student1 = Student("Alice", 85)
# Student2 = Student("Bob", 45)   

# print(Student1.check_result())
# print(Student2.check_result())

class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return print(f"Hello, I am {self.name}!")
    
my_robot = Robot("Robo-X")
my_robot.say_hello()
