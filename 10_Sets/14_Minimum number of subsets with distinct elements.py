'''
Python - Minimum number of subsets with distinct elements using Counter
Story: You have lots of marbles. How many bags do you need so that no bag has two marbles of the same color?
Sample Input:
marbles = ["red", "blue", "red", "green", "blue", "red"]
Sample Output:
3
'''

from collections import Counter

marbles = ["red", "blue", "red", "green", "blue", "red"]
freq = Counter(marbles)
print(max(freq.values()))
