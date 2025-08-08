n = int(input("Enter N: "))

for i in range(1, n + 1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")
