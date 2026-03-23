# i = 1
# while i <= 5:
#     print("Iteration:", i)
#     i += 1
# print("Loop ended.")

# i = 3
# while i>=0:
#     print(i)
#     i = i - 1

# x = 1
# while x <= 100:
#     if x%2 == 0:
#         print(str(x) + " is even")
#     else:
#         print(str(x) + " is odd")

#     x += 1

# i = 0
# while 1==1:
#     print(i)
#     i = i + 1
#     if i >= 5:
#         print("Breaking")
#         break
# print("Finished")

# i = 5
# while True:
#     print(i)
#     i = i -1
#     if i <= 2:
#         break

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
print("Finished")