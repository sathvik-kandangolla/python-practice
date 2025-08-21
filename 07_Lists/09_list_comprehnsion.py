'''List Comprehension
Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
Use list comprehension to create a new list containing fruits with the letter "a".
Convert all fruit names to uppercase using list comprehension.
Replace "banana" with "orange" using list comprehension.'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)

fruits_with_a = [f for f in fruits if "a" in f]
print(fruits_with_a)

fruits_upper = [f.upper() for f in fruits]
print(fruits_upper)

fruits_replaced = [f if f != "banana" else "orange" for f in fruits]
print(fruits_replaced)
