'''Remove all occurrences of a specific element

Input: [1, 2, 3, 2, 4, 2, 5], element = 2
Expected Output: [1, 3, 4, 5]'''

numbers = [1, 2, 3, 2, 4, 2, 5]
result = [x for x in numbers if x != 2]
print(result)
