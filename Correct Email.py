import re

email = input()
result = re.search(r'^[a-zA-Z0-9]+@[a-zA-Z]+[.][a-zA-Z]+', email)

if result and result.group(0) == email:
    print("OK")
else:
    print("WRONG")
