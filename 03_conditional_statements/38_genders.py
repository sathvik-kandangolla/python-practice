age = int(input())
if age > 65:
    print("Senior")
elif 20 <= age <= 65:
    print("Adult")
elif 13 <= age <= 19:
    print("Teen")
elif age < 13:
    print("Child")