blood = input().upper()
if blood == "O-":
    print("Universal donor")
elif blood == "AB+":
    print("Universal recipient")
elif blood in ["A+", "A-", "B+", "B-", "AB-", "O+"]:
    print("Common")
else:
    print("Rare")