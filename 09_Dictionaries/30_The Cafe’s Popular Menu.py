'''
Every order is tracked in a list. Can you build a menu board that shows how many times each item was ordered today?
Input: orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
Expected Output: {'latte': 3, 'espresso': 2, 'tea': 1}

'''
orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
menu = {}

for item in orders:
    menu[item] = menu.get(item, 0) + 1
print(menu)
