import re

a = input()

if re.fullmatch(r"[a-z]+_[a-z]+", a):
    print("Match")
else:
    print("No match")