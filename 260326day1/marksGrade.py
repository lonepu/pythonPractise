user_marks = int(input("Enter you marks:  "))
if user_marks >= 40 and user_marks < 59:
    print("Your grade is F")
elif user_marks >= 60 and user_marks < 69:
    print("Your grade is D")
elif user_marks >= 70 and user_marks < 79:
    print("Your grade is C")
elif user_marks >= 80 and user_marks < 89:
    print("Your grade is B")
elif user_marks >= 90 and user_marks < 95:
    print("Your grade is A")
elif user_marks >= 95 and user_marks <= 100:
    print("Your grade is A+")
elif user_marks <= 39:
    print("You are Fail")
else:
    print("Wrong Input")