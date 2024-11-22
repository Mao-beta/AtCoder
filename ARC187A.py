import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main(N, K, _A):
    A = _A[:]

    if N == 2:
        a, b = _A
        if a <= b:
            return True, [], []
        elif a - b >= K:
            return True, [0], []
        else:
            return False, [], []

    ans = []
    for i in range(1, N-1):
        while A[i-1] > A[i]:
            ans.append(i)
            A[i], A[i + 1] = A[i + 1] + K, A[i]
    if 1 <= A[-2] - A[-1] < K:
        for i in range(N-2, -1, -1):
            ans.append(i)
            A[i], A[i + 1] = A[i + 1] + K, A[i]
        for i in range(1, N - 1):
            while A[i - 1] > A[i]:
                ans.append(i)
                A[i], A[i + 1] = A[i + 1] + K, A[i]
        if A[-2] > A[-1]:
            ans.append(N-2)
            A[-2], A[-1] = A[-1] + K, A[-2]
        i = N - 2
        if A[i-1] > A[i]:
            num = (abs(A[i] - A[i - 1]) + K - 1) // K
            for _ in range(num):
                ans.append(i)
                ans.append(i)
            A[i] += num * K
            A[i + 1] += num * K
        return True, ans, A
    else:
        if A[-2] - A[-1] > 0:
            ans.append(N-2)
            A[-2], A[-1] = A[-1]+K, A[-2]
        if N >= 3 and A[-3] > A[-2]:
            i = N-2
            num = (abs(A[i] - A[i - 1]) + K - 1) // K
            for _ in range(num):
                ans.append(i)
                ans.append(i)
            A[i] += num * K
            A[i + 1] += num * K
        # print(A)
        # print(f"{ans=}")
        return True, ans, A
        # print(A)


from random import randint

if __name__ == "__main__":
    N, K = NMI()
    A = NLI()
    tf, ans, _A = main(N, K, A)
    if tf:
        print("Yes")
        print(len(ans))
        ans = [a+1 for a in ans]
        print(*ans)
    else:
        print("No")

    # for _ in range(1000):
    #     # N = randint(2, 50)
    #     N = 50
    #     K = randint(1, 50)
    #     A = [randint(1, 50) for _ in range(N)]
    #     # print(N, K, A)
    #     tf, ans, _A = main(N, K, A[:])
    #     # if tf:
    #     #     continue
    #     print(N, K, A)
    #     for i in ans:
    #         A[i], A[i+1] = A[i+1] + K, A[i]
    #     print(A)
    #     print(ans)
    #     assert len(ans) <= 500000
    #     assert A == _A
    #     for i in range(N-1):
    #         assert A[i] <= A[i+1]
