# words = ["Hello", "World", "Spam", "Eggs"]
# for word in words:
#     print(word + "!")

# str = "testing for loops"
# count = 0
# for x in str:
#     if x == 't':
#         count += 1
# print("Number of t's:", count)

list = [2,3,4,5,6,7]
for x in list:
    if(x%2 == 1 and x>4):
        print(x)
        break