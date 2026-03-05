import re
a = input()
pat = re.compile(r"^[a]b*$")
print(re.match(pat, a))