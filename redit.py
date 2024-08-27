# Find the expected number of steps to solve snakes and ladders
# Author: Raziman T V (github.com/razimantv)

import numpy as np

N = 100
snakes_ladders = {
    2: 23, 6: 45, 20: 59, 43: 17, 50: 5, 52: 72, 56: 8, 57: 96, 71: 92,
    73: 15, 84: 63, 87: 49, 98: 40
}

# If our move takes us to square i, where do we really end up?
jump = list(range(N))
print (jump)
for start, end in snakes_ladders.items():
    jump[start - 1] = end - 1

# Define E(i) as the expected number of steps to reach end square from square i
# Suppose that we are at square i. We reach square j(x) by rolling 1 <= x <= 6.
# And following any snake/ladder if needed
# Then when i != N, E(i) satisfies
#     E(i) = 1 + [sum_{x=1}^6 E(j(x))] / 6
# If i starts a snake or ladder, then E(i) = E(jump(i))
# Write this in matrix form with the end state E(N) = 0
matrix = np.eye(N)
vector = np.zeros(N)
vector[-1] = 0

for i in range(N - 1):
    if jump[i] != i:
        matrix[i, jump[i]] = -1
        continue
    for x in range(1, 7):
        j = jump[i + x if i + x < N else 2 * (N - 1) - (x + i)]
        matrix[i, j] -= 1 / 6
    vector[i] = 1

# Solve the matrix equation
expectation = np.linalg.solve(matrix, vector)

# Add 6 to incorporate the rule that we only enter the board with a 6
print(f"The expected number of rolls to finish is {expectation[0] + 6:.5}")