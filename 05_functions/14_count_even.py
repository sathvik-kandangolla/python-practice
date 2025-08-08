def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))  
