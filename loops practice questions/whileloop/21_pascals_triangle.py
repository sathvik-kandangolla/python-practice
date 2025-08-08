N = int(input())
row = 0
while row < N:
    num = 1
    for i in range(row + 1):
        print(num, end=" ")
        num = num * (row - i) // (i + 1)
    print()
    row += 1