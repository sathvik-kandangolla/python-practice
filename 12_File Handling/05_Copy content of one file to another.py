'''
Write a program to copy content of one file to another.

Input file (source.txt):

Learning Python
File Handling Practice


Expected output file (destination.txt):

Learning Python
File Handling Practice

'''


with open("source.txt", "r") as src:
    data = src.read()

with open("destination.txt", "w") as dest:
    dest.write(data)
