h = int(input("Enter height: "))

for i in range(1, h + 1):
    spaces = " " * (h - i)
    if i == 1:
        print(spaces + "*")
    elif i == h:
        print("*" * (2 * h - 1))
    else:
        print(spaces + "*" + " " * (2 * i - 3) + "*")
