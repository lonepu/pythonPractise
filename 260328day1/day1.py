message = "The recommended activity is "
temp = int(input("Enter the temperature: "))
if temp > 85:
    message += "swimming"
elif temp > 70:
    message += "tennis"
elif temp > 32:
    message += "goalf"
elif temp > 0:
    message += "dancing"
else:
    message +="sitting by the fire"
print(message)

