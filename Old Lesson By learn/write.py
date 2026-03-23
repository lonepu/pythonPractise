# file = open("testing.txt", "w")
# file.write("This has been written to a file")
# file.close()
#
# file = open("testing.txt", "r")
# print(file.read())
# file.close()

# file = open("newfile.txt", "w")
# file.write("Some new text")
# file.close()
#
# file = open("newfile.txt", "r")
# print("Reading new contents")
# print(file.read())
# print("Finished")
# file.close()

# msg = "Hello wordl!"
# file = open("newfile.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()

# try:
#     f = open("hello.txt")
#     print(f.read())
# finally:
#     f.close()
# try:
#     f = open("hello.txt")
#     print(f.read())
#     print(1 / 0)
# finally:
#     f.close()

# with open("hello.txt") as f:
#     print(f.read())
#
# try:
#     print(1)
#     print(20/0)
#     print(2)
# except ZeroDivisionError:
#     print(3)
# finally:
#     print(4)
try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)