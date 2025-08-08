day = int(input())
if 6 <= day <= 7:
    print("Weekend")
elif 1 <= day <= 5:
    print("Weekday")
else:
    print("Invalid day")