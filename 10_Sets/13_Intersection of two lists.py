'''
Python - Intersection of two lists
Story: Which stickers do you and your friend both have?
Sample Input:
mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]
Sample Output:
{"star", "moon"}

'''

mine = ["dino", "star", "moon"]
yours = ["star", "rocket", "moon"]

print(set(mine) & set(yours))
