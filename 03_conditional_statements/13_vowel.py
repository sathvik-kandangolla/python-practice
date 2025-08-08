letter = input()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
elif letter.isalpha():
    print("Consonant")
else:
    print("Invalid")