temp = int(input())
if temp >= 30:
    print("Hot")
elif 20 <= temp <= 29:
    print("Warm")
elif 10 <= temp <= 19:
    print("Cool")
else:
    print("Cold")