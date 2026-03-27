print("Please Enter an option ")
print("1: Add two numbers")
print("2: Substract two numbers")
print("3: Multiply two numbers")
print("4: Divide two numbers")
print("5: exponentiation two numbers")

z = input("Your Choice: ")
print("\n")

print("Please enter the first number")
a = float(input("First Number: "))
print("Please enter the second number")
b = float(input("Second Number: "))
print("\n")

#if/elif statements to compute the choosen operation

if z == '1':
    c = a+b
    print('a+b = ', c)
elif z == '2':
    c = a-b
    print('a-b = ', c)
elif z == '3':
    c = a*b
    print('axb = ', c)
elif z == '4':
    if a == 0:
        print("Illegal division denominator equals zero")
    else:
        c = a/b
        print('a÷b = ', c)
elif z == '5':
    c = a**b
    print('a^b = ', c)
else:
    print("Worng Input")

print('Bye Bye')

