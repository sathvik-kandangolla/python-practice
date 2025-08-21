'''. Convert List of Strings to Int
input = ["1", "2", "3"] 
expected output=[1,2,3]
'''

str_nums = ["1", "2", "3"]
int_nums = list(map(int, str_nums))
print(int_nums)

