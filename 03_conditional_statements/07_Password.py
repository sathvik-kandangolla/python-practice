password = input()
if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
    print("Strong")
else:
    print("Weak")