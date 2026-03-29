# # Simple Fibonacci Generator
# # Minimal version, no libraries, uses while loop

# print("=" * 40)
# print("   FIBONACCI GENERATOR")
# print("=" * 40)

# while True:
#     print("\n1. Generate sequence")
#     print("2. Exit")

#     choice = input("\nChoose (1-2): ")

#     if choice == "1":
#         try:
#             n = int(input("How many numbers? "))

#             if n <= 0:
#                 print("Please enter positive number!")
#                 continue

#             print("\nFibonacci:", end=" ")

#             if n >= 1:
#                 print("0", end="")

#             if n >= 2:
#                 print(", 1", end="")

#             a, b = 0, 1
#             count = 2

#             while count < n:
#                 a, b = b, a + b
#                 print(f", {b}", end="")
#                 count += 1

#             print()  # New line

#         except ValueError:
#             print("Invalid input!")

#     elif choice == "2":
#         print("\nGoodbye!")
#         break

#     else:
#         print("Invalid choice!")

a, b = 0, 1
while b < 400:
    print(a)
    a, b = b, a + b
