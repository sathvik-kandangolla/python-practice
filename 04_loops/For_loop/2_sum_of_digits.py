n = int(input("Enter a number: "))
sum_digits = 0

for digit in str(n):
    sum_digits += int(digit)

print(f"Sum of digits: {sum_digits}")
