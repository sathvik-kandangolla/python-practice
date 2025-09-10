'''
Write a program to count words in a file.

Input file (words.txt):

Python is easy to learn
File handling is important


Expected Output:

Total words: 8

'''

with open("words.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Total words:", len(words))
