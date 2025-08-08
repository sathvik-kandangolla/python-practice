budget, cost = map(float, input().split())
if cost <= budget:
    print("Within budget")
else:
    print("Over budget")