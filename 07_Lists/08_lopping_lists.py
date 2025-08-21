'''Looping Through Lists
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared.'''

numbers = [1, 2, 3, 4, 5]
print(numbers)

for num in numbers:
    print(num)


i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

squared = [x**2 for x in numbers]
print(squared)
