s1 = "red blue green"
s2 = "blue yellow red"
uncommon = set(s1.split()) ^ set(s2.split())
print( list(uncommon))
