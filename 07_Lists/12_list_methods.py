'''List Methods Practice
Log Session a list: colors = ["red", "green", "blue", "green"].
Use the count() method to find how many times "green" appears.
Use the index() method to find the position of "blue".
Reverse the list using the reverse() method.
Clear the list using the clear() method.'''

colors = ["red", "green", "blue", "green"]
print(colors)

print(colors.count("green"))

print(colors.index("blue"))


colors.reverse()
print(colors)

colors.clear()
print(colors)
