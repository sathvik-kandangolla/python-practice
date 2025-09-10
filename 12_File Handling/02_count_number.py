'''
Write a program to count the number of lines in a file.

Input file (data.txt):

Apple
Banana
Mango
Orange


Expected Output:

Number of lines: 4

'''

with open("data.txt", "r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))
