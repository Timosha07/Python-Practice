import re
a = input().strip()
ab = re.sub(r"([A-Z])", lambda x: f" {x.group(0)} ", a)
print(ab)