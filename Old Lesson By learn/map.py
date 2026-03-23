# def add_five(x):
#     return x +5
# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)
# nums = [11, 22, 33]
# a = list(map(lambda x: x*2, nums))
# print(a)
# nums = [11, 22, 33, 44 ,55]
# res = list(filter(lambda x: x%2==0, nums))
# print(res)
# def countdown():
#     i=5
#     while i > 0:
#         yield i
#         i-=1
# for i in countdown():
#     print(i)
# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
# print(list(numbers(11)))

# def func():
#    i = 100
#    yield i
#
# print(list(func()))
def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word

print(list(make_word()))

