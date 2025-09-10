'''
input :Write a program to create a file and write some text into it

Code
output:Hello, Python!
This is file handling.

'''

with open("sample.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is file handling.\n")
