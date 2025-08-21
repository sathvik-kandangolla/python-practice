'''Sorting and Copying Lists
Log Session a list of numbers: [3, 1, 4, 2, 5].
Sort the list in ascending order.
Sort the list in descending order.
Copy the sorted list to a new list.
Print both lists to verify they are separate copies.'''

numbers = [3, 1, 4, 2, 5]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers_copy = numbers.copy()
print(numbers_copy)

print("Original:", numbers)
print("Copy:", numbers_copy)
