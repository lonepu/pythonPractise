secret_num = "3"

guess = input("Enter a guess for the secret number(1-5)")
if not guess.isdigit():
    print("Invalid: guess should only one digits")
elif guess == "1" or guess == "2":
    print("Guess is too low")
elif guess == "3":
    print("Guess is Correct")
elif guess == "4" or guess == "5":
    print("Guess is too high")
else:
    print(guess, " is not a valid guess (1-5)")
