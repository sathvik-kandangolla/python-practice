'''
A robot does inventory at the end of the day and must tell the boss the total number of items, not just per item. What’s the fastest way for the robot to add up all item counts in the warehouse?
Input: inventory = {'box': 30, 'crate': 22, 'pallet': 8}
Expected Output: Total items in warehouse: 60

'''
north = {'Winterfell': 1000, 'The Eyrie': 800}
south = {'The Eyrie': 1200, "King's Landing": 2500}

north.update(south)
print(north)
