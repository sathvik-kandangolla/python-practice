age = int(input())
if age < 13:
    print("child")
elif 13 <= age <= 19:
    print("teen")
elif 20 <= age <= 64:
    print("adult")
elif age >= 65:
    print("senior")