password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short! It should be at least 8 characters.")
elif password.isalpha():
    print("Digits are missing! Include at least one number.")
else:
    print("Password is strong.")