'''Unzip a list of tuples

Input: [(1, 'a'), (2, 'b'), (3, 'c')]
Expected Output: [1, 2, 3], ['a', 'b', 'c']'''

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*pairs)
print(list(nums))   
print(list(chars))  
