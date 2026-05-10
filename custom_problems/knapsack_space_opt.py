import random
import time


def knapsack_space_opt(pages, cost, funds):
    n = len(pages)
    dp = [0] * (funds + 1)
    for i in range(1, n + 1):
        c = cost[i - 1]
        p = pages[i - 1]
        for j in range(funds, c - 1, -1):
            dp[j] = max(dp[j], dp[j-c] + p)

    return dp[funds]


n = 10 ** 5
pages = [random.randint(0, 100) for _ in range(n)]
cost = [random.randint(1, 20) for _ in range(n)]
funds = 1000
start = time.perf_counter()
print(knapsack_space_opt(pages, cost, funds))
end = time.perf_counter()
print(f'{end - start}s')
