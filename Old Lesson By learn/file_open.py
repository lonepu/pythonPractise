# file = open("hello.txt", "r")
# print(file.read(16))
# print(file.read(4))
# print(file.read(4))
# print(file.read())
# file.close()


# file = open("hello.txt", "r")
# for i in range(21):
#     print(file.read(4))
# file.close()

# file = open("hello.txt", "r")
# file.read()
# print("Re-reading")
# print(file.read())
# print("Finished")
# file.close()
#
# file = open("hello.txt", "r")
# str = file.read()
# print(len(str))
# file.close()
# file = open("hello.txt","r")
# print(file.readlines())
# file.close()
#
# file = open("hello.txt", "r")
#
# for line in file:
#     print(line)
#
# file.close()

file = open("hello.txt","r")
print(len(open("hello.txt").readlines()))