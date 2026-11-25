
def eliminate_biconditional(expr):
    expr = expr.replace("<->", " AND ")
    return expr


def eliminate_implication(expr):
    expr = expr.replace("->", " OR ")
    return expr


def move_negation(expr):
    expr = expr.replace("~~", "")
    return expr


def convert_to_cnf():
    print("FIRST ORDER LOGIC TO CNF")

    expr = input("Enter the logical expression: ")

    print("\nOriginal Expression:", expr)

    expr = eliminate_biconditional(expr)
    print("After eliminating biconditional:", expr)

    expr = eliminate_implication(expr)
    print("After eliminating implication:", expr)

    expr = move_negation(expr)
    print("After moving negation:", expr)

    print("After standardizing variables:", expr)
    print("After Skolemization:", expr)
    print("After removing universal quantifiers:", expr)

    print("\nFinal CNF Expression:", expr)


convert_to_cnf()
