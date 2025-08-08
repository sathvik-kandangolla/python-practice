N = 4
i = 1
num = 1
# Upper Half
while i <= N:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1

i = N - 1
# Lower Half
while i >= 1:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i -= 1
