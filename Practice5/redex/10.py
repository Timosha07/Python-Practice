import re
a = input().strip()
print(re.sub(r"[A-Z]", lambda x: f"_{x.group(0).lower()}", a))