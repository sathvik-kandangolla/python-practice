n = int(input("Enter number: "))

while n >= 10:
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)
    n = sum_digits

print("Digital root:", n)
