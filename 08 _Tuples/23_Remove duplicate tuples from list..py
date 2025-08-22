'''
Description: Remove duplicate tuples from a list of tuples and print the unique tuples only.
This is important for ensuring data integrity and is frequently used in database and data analysis tasks.
Input: lst = [(1, 2), (3, 4), (1, 2), (5, 6)]
Output: [(1, 2), (3, 4), (5, 6)]

'''
lst = [(1, 2), (3, 4), (1, 2), (5, 6)]

result = []
for item in lst:
    if item not in result:
        result.append(item)

print(result)
