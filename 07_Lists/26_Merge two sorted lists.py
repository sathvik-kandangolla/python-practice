'''Merge two sorted lists into one sorted list

Input: [1,3,5], [2,4,6]
Expected Output: [1,2,3,4,5,6]'''

a = [1,3,5]
b = [2,4,6]
merged = sorted(a+b)
print(merged)
