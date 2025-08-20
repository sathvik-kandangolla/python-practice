'''Evaluate Expression in String
Input: "3 + 2*2
Expected Output: 7
'''
def evaluate_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return str(e)
print(evaluate_expression("3 + 2*2"))

