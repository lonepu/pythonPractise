n = int(input("Enter a number: ")) # this is FuzzBuzz program for odd numbers only

for x in range(1, n, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("It is divided by both of 3 and 5")
    elif x % 3 == 0:
        print("It is divided by 3")
    elif x % 5 == 0:
        print("It is divided by 5")
    else:
        print(x)