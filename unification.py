def unify(x, y):
    if x == y:
        return {}

    if x.islower():
        return {x: y}

    if y.islower():
        return {y: x}

    return "FAILURE"


x = input("Enter first expression: ")
y = input("Enter second expression: ")

result = unify(x, y)

print("Unification:", result)