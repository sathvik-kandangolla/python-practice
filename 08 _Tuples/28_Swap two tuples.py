'''Swap two tuples t1=(1,2) and t2=(3,4).
   Convert (1,2,3,4) into integer 1234.
   Output: 1234
'''
t1 = (1,2)
t2 = (3,4)
t1, t2 = t2, t1
print("t1 =", t1)
print("t2 =", t2)
