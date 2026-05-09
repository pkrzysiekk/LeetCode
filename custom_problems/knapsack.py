p = [2, 3, 4, 5, 10]
w = [1, 2, 2, 4, 5]
c = 10


def knapsack(c, n):
    if c == 0 or n == 0:
        return 0
    pick = 0

    if w[n-1] <= c:
        pick = p[n-1] + knapsack(c-w[n-1], n-1)

    notpick = knapsack(c, n-1)
    return max(pick, notpick)


print(knapsack(c, len(p)))
