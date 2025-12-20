# try:
#     num1 = 7
#     num2 = 0
#     print(num1/num2)
#     print("Done calcuation")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
#     print("Please provide a non-zero denominator.")

# try:
#     variable = 10
#     print(10/2)
# except ZeroDivisionError:
#     print("Error")
#     print("Finished")

# try:
#     variable = 10
#     print(variable + "hello")
#     print(variable /2)
# except ZeroDivisionError:
#     print("Divided by zer")
# except(ValueError, TypeError):
#     print("Error occurred")

# try:
#     word = "spam"
#     print(word / 0)
# except:
#     print("An error occurred")

# try:
#     print("Hello")
#     print(1/0)
# except ZeroDivisionError:
#     print("Divided by zero")
# finally:
#     print("This code will run no matter what")

# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)

try:
    print(1)
    print(10/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")


