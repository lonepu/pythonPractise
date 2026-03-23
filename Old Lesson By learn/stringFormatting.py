# # # # # # #String formatting
# # # # # # # nums = [4, 5, 6]
# # # # # # # msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
# # # # # # # print(msg)
# # # # # #
# # # # # # # print("{0}{1}{0}".format("abra", "cad"))
# # # # # # a = "{x}, {y}".format(x=5, y=12)
# # # # # # print(a)
# # # # # # b = "{firstname},{lastname}".format(firstname="John", lastname="Doe")
# # # # # # print(b)
# # # # # str="{c},{b},{a}".format(a=5, b=9, c=7)
# # # # # print(str)
# # # # print('Hello Me'.replace("Me", "world"))
# # # # print('This is a sentence.'.startswith("This"))
# # # # print('This is a sentence.'.endswith("sentence."))
# # # # print('This is a sentence.'.upper())
# # # # print('AN ALL CAPS SENTENCE'.lower())
# # # # print('spam, eggs, ham'.split(', '))
# # # print(min(1, 2, 3, 4, 0, 2, 1))
# # # print(max([1, 4, 9, 2, 5, 6, 8]))
# # # print(abs(-99))
# # # print(abs(42))
# # # # print(sum([1, 2, 3, 4, 5]))
# # # print(sum([11,22]))
# # # print(max(abs(-30),2))
# # # a=min([sum([11,22]), max(abs(-30),2)])
# # # print(a)
# # nums = [55, 44, 33, 22, 11]
# # if all([i > 5 for i in nums]):
# #     print("All larger than 5")
# #
# # if any([i % 2 == 0 for i in nums]):
# #     print("At least one is even")
# #
# # for v in enumerate(nums):
# #     print(v)
# nums = [-1, 2, -3, 4, -5]
# if all([abs(i)<3 for i in nums]):
#     print(1)
# else:
#     print(2)
filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

    print(text)