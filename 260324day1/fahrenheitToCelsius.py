user_input = input("Enter a Temperature in Fahrenheit: ")
if not user_input.isnumeric():
    print("Invalid input. Please enter a numeric value.")
else:
    celsius = (float(user_input) - 32) * 5 / 9
    print(f"{user_input} ℉ is equal to {celsius:.2f} ℃.")