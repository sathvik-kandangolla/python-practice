temp =int(input("Enter temperature: "))
if temp <= 0:
    print("solid")
elif temp >= 0 and temp <= 100:
    print("liquid")
else:
    print("gas")