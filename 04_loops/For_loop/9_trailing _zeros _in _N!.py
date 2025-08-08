n = int(input("Enter N: "))
count = 0
divisor = 5

while n // divisor:
    count += n // divisor
    divisor *= 5

print(f"Trailing zeros in {n}!: {count}")
