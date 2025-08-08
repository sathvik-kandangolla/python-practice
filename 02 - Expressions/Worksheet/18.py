n=150
k=2
rotated=((n<< k)  | (n >>(8-k))) &0xFF
print(rotated)
