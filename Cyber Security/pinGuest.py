import random

secret_pin = input("Enter your pin: ")# that user wants to set
guess = ""
attempts = 0

while guess != secret_pin:
    # computer is making random guesses
    guess = str(random.randint(1000, 9999))
    attempts += 1

print(f"Hacker is able to hack the pin {secret_pin} in {attempts} attempts.")
