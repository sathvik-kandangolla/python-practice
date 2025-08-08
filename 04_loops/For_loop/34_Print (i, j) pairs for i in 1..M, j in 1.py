m = int(input("Enter M: "))
k = int(input("Enter K: "))
t = int(input("Enter threshold T: "))

i = 1
stop = False

while i <= m and not stop:
    j = 1
    while j <= k:
        if i * j > t:
            stop = True
            break
        print(f"({i},{j})")
        j += 1
    i += 1
