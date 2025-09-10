'''
: Check if String is Binary

Input:

note = "101010"


Expected Output:

Yes
'''
note = "101010"
if set(note) <= {"0", "1"}:
    print("Yes")
else:
    print("No")

