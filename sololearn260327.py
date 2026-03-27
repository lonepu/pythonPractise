# import re
# pattern = r"spam"
# if re.match(pattern, "spamspamspam"):
#     print("Match")
# else:
#     print("No match")

# import re
# pattern = r"spam"
# if re.match(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")
# if re.search(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")
# print(re.findall(pattern, "eggspamsausagespam"))

# import re
# pattern = r"pam"
# match = re.search(pattern, "eggspamsausage")
# if match:
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print(match.span())

# import re

# str = "My name is David. Hi David."
# pattern = r"David"
# newstr = re.sub(pattern, "Amy", str)
# print(newstr)

# import re
# pattern = r"gr.y"
# if re.match(pattern, "grey"):
#     print("Match 1")
# if re.match(pattern, "gray"):
#     print("Match 2")
# if re.match(pattern, "blue"):
#     print("Match 3")

# import re
# pattern = r"^gr.y$"
# if re.match(pattern, "grey"):
#     print("Match 1")
# if re.match(pattern, "gray"):
#     print("Match 2")
# if re.match(pattern, "stringray"):
#     print("Match 3")

# import re
# pattern = r"[aeiou]"
# if re.search(pattern, "grey"):
#     print("Match 1")
# if re.search(pattern, "qwertyuiop"):
#     print("Match 2")
# if re.search(pattern, "rhythm myths"):
#     print("Match 3")

# import re
# pattern = r"[A-Z][A-Z][0-9]"

# if re.search(pattern, "LS8"):
#     print("Match 1")
# if re.search(pattern, "E3"):
#     print("Match 2")
# if re.search(pattern, "lab"):
#     print("Match 3")

# import re
# pattern = r"[^A-Z]"
# if re.search(pattern, "This is all quiet"):
#     print("Match 1")
# if re.search(pattern, "AbCdEfG123"):
#     print("Match 2")
# if re.search(pattern, "THISISALLSHOUTING"):
#     print("Match 3")

import re
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")