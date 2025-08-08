n = int(input("Enter N: "))
cum_sum = 0

for i in range(1, n + 1):
    even = 2 * i
    cum_sum += even
    print(f"{even} (Sum: {cum_sum})")
