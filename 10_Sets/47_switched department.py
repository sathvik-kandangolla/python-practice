'''
Employees who switched departments
input:

deptA = {"John", "Alice", "Bob"}
deptB = {"Alice", "David", "Bob"}



Expected Output:

{'Alice', 'Bob'}

'''
deptA = {"John", "Alice", "Bob"}
deptB = {"Alice", "David", "Bob"}
switched = deptA & deptB
print(switched)
