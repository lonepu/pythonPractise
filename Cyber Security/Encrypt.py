message = input("Enter Your Message: ")
secret_message = ""

for letter in message:
    #changing the value of each letter by 3
    new_char = chr(ord(letter) + 3)
    secret_message += new_char

print("Encrypted Code -", secret_message)