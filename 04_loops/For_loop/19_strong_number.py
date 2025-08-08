n = int(input("Enter a number: "))
temp = n
sum_fact = 0

for digit in str(n):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    sum_fact += fact

print("Strong number" if sum_fact == temp else "Not a strong number")
