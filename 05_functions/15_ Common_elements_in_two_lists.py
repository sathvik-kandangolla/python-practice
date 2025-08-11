def common(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(common([1, 2, 3], [2, 3, 4]))  
