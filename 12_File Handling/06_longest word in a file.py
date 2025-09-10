'''
Write a program to find the longest word in a file.

Input file (words.txt):

cat
elephant
dog
tiger


Expected Output:

Longest word: elephant

'''


with open("words.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)
