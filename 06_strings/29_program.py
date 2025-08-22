'''Remove Consecutive Duplicates

Input1: "abc bca dca acb"
input2: "bca axz 2ab dca"
Expected Output: "abc acb axz 2ab"'''

# Inputs
input1 = "abc bca dca acb"
input2 = "bca axz 2ab dca"

# Step 1: Convert the strings into lists of words
list1 = input1.split()   # ['abc', 'bca', 'dca', 'acb']
list2 = input2.split()   # ['bca', 'axz', '2ab', 'dca']

# Step 2: Convert lists to sets (to easily compare unique elements)
set1 = set(list1)
set2 = set(list2)

# Step 3: Find words that are only in one of the sets (symmetric difference)
unique_words = set1.symmetric_difference(set2)

# Step 4: Convert back to string
output = " ".join(unique_words)

print(output)   # abc acb axz 2ab






