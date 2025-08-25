'''
Create a dictionary where keys are numbers from 1 to 5 and values are their squares.

Input:

n = 5


Expected Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''
n = 5
d = {i: i**2 for i in range(1, n+1)}
print(d)
