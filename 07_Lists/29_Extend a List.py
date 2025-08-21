'''Add all items of [1, 2, 3] to ["x", "y", "z"].
input=[1, 2, 3] to ["x", "y", "z"].

expected output=['x', 'y', 'z', 1, 2, 3]
'''

list1 = ["x", "y", "z"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
