N = int(input("Enter a number: "))
i = 1
while i <= N:
    if str(i) == str(i)[::-1]:  
        print(i, end=" ")
    i += 1