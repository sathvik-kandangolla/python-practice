'''Find common elements between two lists

Input: [1, 2, 3, 4], [3, 4, 5, 6]
Expected Output: [3, 4]'''

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list(set(list1) & set(list2)))

