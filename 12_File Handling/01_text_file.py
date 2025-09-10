'''
Write a program to read a text file and print its contents.

Input file (sample.txt):

Hello Python
File handling example


Expected Output:

Hello Python
File handling example

'''


with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
