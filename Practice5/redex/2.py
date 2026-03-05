import re
a = input()
pat=re.compile(r"^ab+$")
print(re.match(pat, a))