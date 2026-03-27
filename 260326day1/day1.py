# num = 12
# if num > 5:
#     print("Bigger tham 5")
#     if num <= 47:
#         print("Between 5 and 47")

# num = 7
# if num > 3:
#     print("3")
#     if num < 5:
#         print("5")
#         if num == 7:
#             print("7")

# x = 4
# if x == 5:
#     print("Yes")

# else:
#     print("No")

# if 1+1==2:
#     if 2*2==8:
#         print("if")
#     else:
#         print("else")

# num = 3
# if num == 3:
#     print("One")
# else:
#     if num ==2:
#         print("Two")
#     else:
#         if num ==3:
#             print("Three")
#         else:
#             print("Something else")

# num = 3
# if num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:
#     print("Three")
# else:
#     print("Error")

# user_marks = int(input("Enter you marks:  "))
# if user_marks >= 40 and user_marks < 59:
#     print("Your grade is F")
# elif user_marks >= 60 and user_marks < 69:
#     print("Your grade is D")
# elif user_marks >= 70 and user_marks < 79:
#     print("Your grade is C")
# elif user_marks >= 80 and user_marks < 89:
#     print("Your grade is B")
# elif user_marks >= 90 and user_marks < 95:
#     print("Your grade is A")
# elif user_marks >= 95 and user_marks <= 100:
#     print("Your grade is A+")
# elif user_marks <= 39:
#     print("You are Fail")
# else:
#     print("Wrong Input")

# if(1==1) and (2+2>3):
#     print("true")
# else:
#     print("false")

# name = (input("Enter your username: "))
# password = (input("Enter your password: "))

# if (name == "Htet Myet" and password =="Pas$w0rd123!"):
#     print(f"Welcome Mr.{name}")
# else:
#     print("Wrong Username or Password! Try Again")

# i = 1
# while i <= 3:
#     print(i)
#     i +=1

# print("Finished")#while looping is Time Saver

# user_input = int(input("Enter your numbers: "))

# while user_input!=10:
#     print("Your input num is not equal to 10")
#     print("Please try again! ")
#     user_input = int(input("Enter your number: "))
# print("Thank You")
# print("Your enter value is 10")

# x = 1
# while x < 10:
#     if x%2==0:
#         print(str(x) + " is even ")
#     else:
#         print(str(x) + " is odd ")
#     x+=1

# x = 0
# while x<=20:
#     print(x)
#     x +=2

# i = 5
# while True:
#     print(i)
#     i -= 1
#     if i <= 2:
#         print("Breaking")
#         break
# print("Finished")

# user_input = input("Say something: ")
# while True:
#     user_input = input("Say something: ")
#     if user_input == "quit":
#         print("Program Stop!!!")
#         break
#     print("The lenght of your says is ", len(user_input))

# while True:
#     a = input("Enter Something ")
#     if a == "quit":
#         break
#     print('Length of the string is ', len(a))
# print("Done!")

# i = 1
# while i <= 5:
#     print(i)
#     i+=1
#     if i==3:
#         print('Skipping 3')
#         continue

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#     if i == 7:
#         print("Skipping 7")
#         continue

while True:
    a = input("Enter Something: ")
    if a == 'quit':
        break

    if len(a) <3:
        print('Too Small')
        continue
    print("Input is sufficient length ", len(a))