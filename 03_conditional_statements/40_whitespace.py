char = input()
if char.isdigit():
    print("digit")
elif char.isalpha():
    print("letter")
elif char.isspace():
    print("space")
else:
    print("other")