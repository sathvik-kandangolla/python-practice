def multiplication_table(num, i=1):
    if i > 10:
        return
    print(f"{num} x {i} = {num * i}")
    multiplication_table(num, i + 1)

multiplication_table(5)
