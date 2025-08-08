def factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

n = 4
for i in range(n):
    for j in range(i+1):
        val = factorial(i) // (factorial(j) * factorial(i-j))
        print(val, end="")
    print()
