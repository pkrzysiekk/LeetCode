import random
import time


def knapsack_space_opt(val, wt, cap):
    n = len(val)
    dp = [0] * (cap + 1)
    for i in range(1, len(wt)):
        for j in range(cap, wt[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j-wt[i-1]] + val[i-1])

    return dp[cap]


n = 10 ** 5
val = [random.randint(0, 100) for _ in range(n)]
wt = [random.randint(1, 20) for _ in range(n)]
cap = 1000
start = time.perf_counter()
print(knapsack_space_opt(val, wt, cap))
end = time.perf_counter()
print(f'{end - start}s')
