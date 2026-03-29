calculator_name= """BMI Calculator
===============\n"""
print(calculator_name)

weight=float(input("Enter your weight in KG: "))
height=float(input("Enter your height in cm: "))

user_bmi = weight/((height*0.01)**2)

if user_bmi < 18.5:
    print("Your are Underweight")
elif user_bmi >=18.5 and user_bmi<25:
    print("Your are Normal")
elif user_bmi >=25 and user_bmi <30:
    print("Your are Overweight")
elif user_bmi >30:
    print("You need to check with Doctor! Your are Obesity")
else:
    print("Wrong Input")

