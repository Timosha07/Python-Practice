import re
a = input()
pat = re.compile(r"\b[A-Z][a-z]+\b")
print(re.findall(pat, a))