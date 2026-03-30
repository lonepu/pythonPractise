print("Sample Calculator")

print("=" * 20)

first_number = input("first Number? ")

if first_number.isnumeric() == False:
    print("Please Input a number!")
    exit()

operation = input("Operator: ")

second_number = input("Second Number? ")

if second_number.isnumeric() == False:
    print("Please Input a number!")
    exit()

first = int(first_number)
second = int(second_number)
result = 0

if operation == "+":
    result = first + second
    lable = "sum"
elif operation == "-":
    result = first - second
    lable = "difference"
elif operation == "*":
    result = first * second
    lable = "product"
elif operation == "/":
    result = first / second
    lable = "quotient"
elif operation == "**":
    result = first**second
    lable = "exponent"
elif operation == "%":
    result = first % second
    lable = "modulus"
else:
    print("Invalid Operator!")
    exit()
print("=" * 40)
print(f"The {lable} of {first} and {second} is: {result}")
print("=" * 40)
