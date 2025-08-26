'''
Python program to find union of n arrays
Story: Collect favorite colors from all your classmates—what are all the colors?
Sample Input:
friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]
Sample Output:
{'red', 'blue', 'green', 'yellow'}

'''
friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]

all_colors = set().union(*friends_colors)
print(all_colors)
