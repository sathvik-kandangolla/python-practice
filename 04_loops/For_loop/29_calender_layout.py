start_day = int(input("Enter starting day (0=Sun, 6=Sat): "))
day = 1

# Print leading spaces
for _ in range(start_day):
    print("   ", end="")

while day <= 31:
    print(f"{day:2d} ", end="")
    if (start_day + day) % 7 == 0:
        print()
    day += 1
