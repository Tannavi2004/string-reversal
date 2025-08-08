import re

def check_pwd(p):
    rules = [
        len(p) >= 8,
        re.search(r'[A-Z]', p),
        re.search(r'[a-z]', p),
        re.search(r'\d', p),
        re.search(r'[!@#$%^&*()]', p)
    ]
    return all(rules)

pwd = input("Enter password: ")
print("Strong!" if check_pwd(pwd) else "Weak password.")
