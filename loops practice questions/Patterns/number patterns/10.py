n = 7
for i in range(1, n+1):
    print("".join(str(j) for j in range(1, i+1)), end="")
    print("*" * (n - i))
