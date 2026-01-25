# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))
#
# def test(func, arg):
#     return func(func(arg))
# def mult(x):
#     return x*x
# print(test(mult,2))

# def pure_function(x, y):
#     temp = x + 2*y
#     return temp/(2*x +y)
#
# some_list = []
# def impure(arg):
#     some_list.append(arg)

#named function
# def polynomial(x):
#     return x**2 + 5*x + 4
# print(polynomial(-4))
#
# #lambda
# print((lambda x: x**2 + 5*x + 4) (-4))
# double = lambda x: x* 2
# print(double(7))
triple = lambda x: x*3
add = lambda x, y: x + y
print(add(triple(3), 4))