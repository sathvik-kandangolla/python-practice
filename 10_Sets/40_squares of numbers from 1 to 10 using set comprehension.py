'''
Write a Python program to create a set of the squares of numbers from 1 to 10 using set comprehension.
input :
(1,2,3,4,5,6,7,8,9,10)

Output:

{1, 4, 9, 16, 25, 36, 49, 64, 81, 100}

'''
squares = {x**2 for x in range(1, 11)}
print(squares)
