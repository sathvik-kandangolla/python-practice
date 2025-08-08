def gcd(a, b):#greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))

