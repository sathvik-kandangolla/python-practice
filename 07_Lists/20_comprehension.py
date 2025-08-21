'''Create list of even numbers using comprehension

Input: [1,2,3,4,5,6,7,8,9,10]
Expected Output: [2, 4, 6, 8, 10]'''

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [x for x in numbers 
         if x % 2 == 0]
print(evens)
