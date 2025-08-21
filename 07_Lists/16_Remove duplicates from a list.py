'''Remove duplicates from a list

Input: [1, 2, 3, 2, 4, 3, 5]
Output: [1, 2, 3, 4, 5]'''

numbers = [1, 2, 3, 2, 4, 3, 5]
unique = list(set(numbers))
print(unique)   
