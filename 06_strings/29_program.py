'''Remove Consecutive Duplicates

Input1: "abc bca dca acb"
input2: "bca axz 2ab dca"
Expected Output: "abc acb axz 2ab"'''

input1 = "abc bca dca acb"
input2 = "bca axz 2ab dca"

# Split inputs into lists of words
list1 = input1.split()
list2 = input2.split()

# Keep words that are unique to each list
unique_words = [word for word in list1 + list2 if (word in list1 and word not in list2) ]

output = " ".join(unique_words)
print(output)





