username = input()
if len(username) >= 3 and not username[0].isdigit():
    print("Valid")
else:
    print("Invalid")