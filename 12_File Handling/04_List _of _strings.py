'''
Write a program to write a list of strings into a file.

Input (list of strings):

lines = ["Python", "Java", "C++", "JavaScript"]


Expected file content (output.txt):

Python
Java
C++
JavaScript

'''

lines = ["Python", "Java", "C++", "JavaScript"]

with open("output.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
