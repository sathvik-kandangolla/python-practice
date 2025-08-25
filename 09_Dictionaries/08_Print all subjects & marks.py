'''
Print all subjects & marks.
Input: student = {'math': 90, 'english': 88, 'science': 92}
Expected Output:math 90
english 88
science 92

'''
student = {'math': 90, 'english': 88, 'science': 92}
for sub, mark in student.items():
    print(sub, mark)
