import re

def check(string):
    pattern = r"[a-z]+@gmail\.com"
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

n = input()
print(check(n))