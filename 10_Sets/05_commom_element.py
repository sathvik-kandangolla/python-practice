'''
Python - Check if two lists have at-least one element common
Story: You and your friend want to see if you both like any of the same cartoons.
Sample Input:
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
Sample Output:
Yes! "Jerry" is common.

'''

my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]

if set(my_favs) & set(friend_favs):
    print("Yes! Common:", set(my_favs) & set(friend_favs))
else:
    print("No common elements.")
