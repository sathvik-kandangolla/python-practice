n = int(input("Enter N: "))
i = 1

while i <= n:
    j = 1
    while j <= n:
        if i + j <= n:
            print(f"({i},{j})")
        j += 1
    i += 1
