status = int(input())
if 200 <= status <= 299:
    print("success")
elif 300 <= status <= 399:
    print("redirect")
elif 400 <= status <= 499:
    print("client error")
elif 500 <= status <= 599:
    print("server error")
else:
    print("unknown")