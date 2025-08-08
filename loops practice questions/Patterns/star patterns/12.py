# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end="")
#     print()



# n = 4
# for i in range(n):
#     for j in range(i + 1):
#         if j % 2 == 0:
#             print(1, end="")
#         else:
#             print(2, end="")
#     print()






n = 4
for i in range(n):
    for j in range(i + 1):
        
        if i % 2 == 0:
            num = 1 if j % 2 == 0 else 2
        else:
            num = 2 if j % 2 == 0 else 1
        print(num, end=" ")
    print()