# import re

# pattern = r"egg(spam)*"
# if re.match(pattern, "egg"):
#     print("Match 1")
# if re.match(pattern, "eggspamspamegg"):
#     print("Match 2")
# if re.match(pattern, "spam"):
#     print("Match 3")

# import re

# pattern = r"g+"
# if re.match(pattern, "g"):
#     print("Match 1")
# if re.match(pattern, "ggggggggggggg"):
#     print("Match 2")
# if re.match(pattern, "abc"):
#     print("Match 3")

# import re

# pattern = r"ice(-)?cream"
# if re.match(pattern, "ice-cream"):
#     print("Match 1")
# if re.match(pattern, "icecream"):
#     print("Match 2")
# if re.match(pattern, "sausages"):
#     print("match 3")
# if re.match(pattern, "ice--ice"):
#     print("Match 4")

# import re

# pattern = r"9{1,3}$"
# if re.match(pattern, "g"):
#     print("Match 1")
# if re.match(pattern, "999"):
#     print("Match 2")
# if re.match(pattern, "9999"):
#     print("Match 3")

# import re

# pattern = r"egg(spam)*"
# if re.match(pattern, "egg"):
#     print("Match 1")
# if re.match(pattern, "eggspamspamegg"):
#     print("Match 2")
# if re.match(pattern, "spam"):
#     print("Match 3")

# import re

# pattern = r"a(bc)(de)(f(g)h)i"
# match = re.match(pattern, "abcdefghijklmnop")
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group())

# import re
# pattern = r"1(23)(4(56)78)9(0))"
# match = re.match(pattern, "1234567890")
# if match:
#     print(match.group(3))

# import re

# pattern = r"(?P<first>abc)(?:def)(ghi)"
# match = re.match(pattern, "abcdefghi")
# if match:
#     print(match.group("first"))
#     print(match.groups())

# import re

# pattern = r"gr(a|e)y"
# match = re.match(pattern, "gray")
# if match:
#     print("Match 1")
# match = re.match(pattern, "grey")
# if match:
#     print("Match 2")
# match = re.match(pattern, "griy")
# if match:
#     print("Match  3")

# import re

# patterns = [r"(1|2|3|4|5)", r"[12345]", r"[1-6]"]
# test_numbers = ["1", "2", "3", "4", "5", "6", "0", "7"]
# for i, pattern in enumerate(patterns):
#     print(f"\nPattern {i+1}: {pattern}")
#     print("-" * 30)
#     for num in test_numbers:
#         if re.match(pattern, num):
#             print(f"   Matches: {num}")
#         else:
#             print(f"   No match: {num}")

# import re

# pattern = r"(.+) \1"
# a = "word word"
# b = "?! ?!"
# c = "abc cde"
# match = re.match(pattern, a)
# if match:
#     print("Match 1")
# match = re.match(pattern, b)
# if match:
#     print("Match 2")
# match = re.match(pattern, c)
# if match:
#     print("Match 3")

# import re

# pattern = r"(\D+\d)"
# a = "Hi 999!"
# b = "1, 23, 456!"
# c = "! $?"

# match = re.match(pattern, a)
# if match:
#     print("Match 1")
# match = re.match(pattern, b)
# if match:
#     print("Match 2")
# match = re.match(pattern, c)
# if match:
#     print("Match 3")

import re

pattern = r"\b(cat)\b"
a = "The cat sat!"
b = "We s>cat<tered?"
c = "We scattered."

match = re.search(pattern, a)
if match:
    print("Match 1")
match = re.search(pattern, b)
if match:
    print("Match 2")
match = re.search(pattern, c)
if match:
    print("Match 3")
