
def alpha_beta(depth, node, maximizing, values, alpha, beta):

    if depth == 2:
        return values[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i,
                             False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i,
                             True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best



print("ALPHA-BETA PRUNING")

values = []

print("Enter 4 leaf node values:")

for i in range(4):
    n = int(input("Enter value " + str(i + 1) + ": "))
    values.append(n)

result = alpha_beta(0, 0, True, values,
                    float('-inf'), float('inf'))

print("\nOptimal value is:", result)
