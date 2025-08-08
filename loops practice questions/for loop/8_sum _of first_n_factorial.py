
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    total += fact

print(f"Sum of first {n} factorials: {total}")