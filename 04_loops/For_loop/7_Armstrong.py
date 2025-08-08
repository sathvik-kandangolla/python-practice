n = int(input("Enter a number: "))
num_str = str(n)
power = len(num_str)
sum_armstrong = sum(int(digit) ** power for digit in num_str)

print("Armstrong Number" if sum_armstrong == n else "Not Armstrong")
