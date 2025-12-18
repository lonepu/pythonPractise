# def max(x, y):
#     if x>=y:
#         return x
#     else:
#         return y
    
# print("the Max num is :", max(4,7))
# z=max(8,5)
# print("the Max num is :", z)

# def add_numbers(x, y):
#     total = x + y
#     return total
# print("This won't be printed")

# print(add_numbers(4, 5))

# def print_numbers():
#     print(1)
#     print(2)
#     return  
# print(4) 
# print(6)
# print_numbers()

# x = 365
# y = 7
# # this is a comment

# print(x%y) # find the remainder
# #print(x//y) 
# #another comment

# def shout(word):
#     """
#     Print a word with an 
#     exclammation mark following it.
#     """
#     print(word + "!")

# shout("congratulations")

# def multiply(x, y):
#     return x * y
# a = 4
# b = 7
# opeartion = multiply
# print(opeartion(a, b))

# def add(x, y):
#     return x + y
# def do_twice(func, x, y):
#     return func(func(x, y), func(x, y))

# a = 5
# b = 10

# print(do_twice(add, a, b))

def square(x):
    return x * x
def test(func, x):
    print(func(x))
test(square, 42)
