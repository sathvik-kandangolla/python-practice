N = 4
width = 4
i = 0
num = 1
while i < N:
    j = 0
    if i % 2 == 0:  # Even row - Left to Right
        while j < width:
            print(num, end=" ")
            num += 1
            j += 1
    else:  # Odd row - Right to Left
        temp = []
        while j < width:
            temp.append(num)
            num += 1
            j += 1
        while temp:
            print(temp.pop(), end=" ")
    print()
    i += 1
