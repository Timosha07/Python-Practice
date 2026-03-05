import re
a = input()
pat = re.compile(r"[.,\s]")
print(re.sub( pat, "|", a))