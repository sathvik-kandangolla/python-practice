'''Find all sublists of a list

Input: [1, 2, 3]
Expected Output: [[],[1],[2],[3],[1,2],[2,3],[1,2,3]]'''

lst = [1,2,3]
sublists = [[]]
for i in range(len(lst)):
    for j in range(i+1, len(lst)+1):
        sublists.append(lst[i:j])
print(sublists)
