import random
import time


def knapsack_bottom(val, wt, cap):
    n = len(val)
    dp = [[0 for _ in range(cap + 1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(cap+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w], val[i - 1] + dp[i-1][w-wt[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][cap]


start = time.perf_counter()
n = 10 ** 5
val = [random.randint(0, 100) for _ in range(n)]
wt = [random.randint(1, 20) for _ in range(n)]
cap = 1000
print(knapsack_bottom(val, wt, cap))
end = time.perf_counter()
print(f'{end - start}s')
