# try:
#     print(1/0)
# except ZeroDivisionError:
#     raise ValueError

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     elif age < 18:
#         return "Minor"
#     else:
#         return "Adult"
    
# try:
#     result = check_age(20)
#     print(result)
# except ValueError as e:
#     print("Caught an exception:", e)

# name = "123"
# raise NameError("Invalid name!")

try:
    name = 5/ 0 
except:
    print("An error occurred")
    raise