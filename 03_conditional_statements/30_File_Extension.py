ext = input()
if ext == ".txt":
    print("text/plain")
elif ext == ".jpg":
    print("image/jpeg")
elif ext == ".html":
    print("text/html")
else:
    print("application/octet-stream")