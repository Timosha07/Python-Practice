import re
a = input()
pat = re.compile(r"a.*b$\b")
print(re.findall(pat, a))