'''Joining and Extending Lists
Log Session two lists: list1 = ["a", "b", "c"] and list2 = [1, 2, 3].
Concatenate the two lists into a new list.
Use the extend() method to add list2 to list1.
Print the final lists.'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1)
print(list2)


combined = list1 + list2
print(combined)


list1.extend(list2)
print(list1)


print("list1:", list1)
print("list2:", list2)
