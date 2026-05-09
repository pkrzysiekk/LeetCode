def LIS(A):
    L = [1] * len(A)

    for i in range(1, len(A)):
        for k in range(i):
            if A[k] < A[i]:
                L[i] = max(L[i], L[k] + 1)

    return max(L, default=0)


print(LIS([1, 2, 3]))
