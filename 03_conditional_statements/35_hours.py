hour = int(input())
if 5 <= hour <= 11:
    print("Morning")
elif 12 <= hour <= 17:
    print("Afternoon")
elif 18 <= hour <= 21:
    print("Evening")
else:
    print("Night")