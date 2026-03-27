"""flow control
DecisionMaking
if(expression):True/False

If the user maintained a bank account balance over $1000 waive the transaction fees
If a user cancels their appointment less than 24 hours before the appointment, charge a cancellation fee
If the hockey player gets the puck in the net, add one to the score
"""

# answer = input("Would you like express shipping?")
# if answer == "yes":
#     print("That will be an extra $10")
# else:
#     print("Have a nice day")

# password = input("Enter your password! :")
# if password == "password" and len(password)==8:
#      print("Your password is correct")
# else:
#      print("Your password is not correct!!")

# x = 42
# if x > 5:
#     print("x is greater than 5")

# spam = 7
# if spam > 5:
#     print("five")
# if spam > 8:
#     print("eight")

hour_worked = int(input("Enter Working Hour: "))
rate = 25.00
if hour_worked > 40:
    grossPay = (40*rate) + ((hour_worked-40)*(rate * 1.5))
if hour_worked <=40:
    grossPay = hour_worked * rate
print("Gross Pay: " + str(grossPay))