#
# import this
# from this import s

# print(s)

# def my_func(x, y=7, *args, **kwargs):
#     print(kwargs)

# my_func(2,3,4,5,6, a=7, b=8)


# kwargs က dictionary ဖြစ်လို့ ဒီလိုလုပ်လို့ရ
# def my_func(**kwargs):
#     kwargs["new_key"] = "new_value"  # ထပ်ထည့်လို့ရ
#     del kwargs["old_key"]  # ဖျက်လို့ရ
#     kwargs.update({"x": 10})  # update လုပ်လို့ရ


# ဒါပေမဲ့ set လိုမဟုတ်ဘူး
# kwargs = {1, 2, 3}  # ဒီလိုမဟုတ်ဘူး

# numbers = (1, 2, 3)
# a, b, c = numbers
# print(a)
# print(b)
# print(c)

# x, y = [1, 2]
# x, y = y, x
# print(y)
# print(x)

# a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(b)
# print(c)
# print(d)

# a, b, c, d, *e, f, g = range(20)
# print(range(20))
# print(e)
# print(len(e))

# a = 7
# b = 1 if a >= 5 else 42
# print(b)

# status = 1
# msg = "Logout" if status == 1 else "Login"
# print(msg)

# b = 1 if 2 + 2 == 5 else 2
# print(b)

# for i in range(10):
#     if i == 999:
#         break
# else:
#     print("Unbroken 1")
# for i in range(10):
#     if i == 5:
#         break
# else:
#     print("Unbroken 2")

# for i in range(10):
#     if i > 5:
#         print(i)
#         break
#     else:
#         print("7")

# try:
#     print(1)
# except ZeroDivisionError:
#     print(2)
# else:
#     print(3)

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print(4)
# else:
#     print(5)

# try:
#     print(1)
#     print(1 + "1" == 2)
#     print(2)
# except TypeError:
#     print(3)
# else:
#     print(4)


# def function():
#     print("This is a module function.")


# if __name__ == "__main__":
#     print("This is a script")

# x = 1
# y = x
# if __name__ == "__main__":
#     z = 3


# def function():
#     print("this is a module function.")


# if __name__ == "__main__":
#     print("this is a script:")


# def func(**kwargs):
#     print(kwargs["zero"])


# func(a=0, zero=8)

# for i in range(10):
#     try:
#         if 10 / i == 2.0:
#             break
#     except ZeroDivisionError:
#         print(1)
#     else:
#         print(2)
a = 7
b = 42
a, b = b, a
print(a, b)
