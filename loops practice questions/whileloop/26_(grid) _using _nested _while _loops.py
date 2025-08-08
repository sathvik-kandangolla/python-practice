N = int(input())
i = 1   
while i <= N:
    j = 1
    while j <= N:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1