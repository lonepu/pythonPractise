celsius = int(input("Enter Your Temperature: "))
def conv(c):
    #your code goes here
    return (c * 9/5) + 32
fahrenheit = (conv(celsius))
print("The temperature in Fahrenheit is:", fahrenheit)