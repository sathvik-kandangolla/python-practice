'''
Increase salaries by 10%.
Input: salaries = {'A': 20000, 'B': 30000}
Expected Output: {'A': 22000.0, 'B': 33000.0}

'''
salaries = {'A': 20000, 'B': 30000}
for k in salaries:
    salaries[k] *= 1.1
print(salaries)
