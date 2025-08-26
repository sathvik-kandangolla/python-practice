'''
Python program to find the difference between two lists
Story: What games do you want to play this week that you didn't play last week?
Sample Input:
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]
Sample Output:
["jump", "run"]

'''
last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]

diff = set(this_week) - set(last_week)
print(list(diff))
