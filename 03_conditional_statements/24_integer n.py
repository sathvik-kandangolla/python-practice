n = int(input())
if n % 2 == 0 and abs(n) < 10:
    print("even small")
elif n % 2 == 0 and abs(n) > 10:
    print("even large")
else:
    print("odd large")