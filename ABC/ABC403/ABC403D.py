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


def main(N, D, A):
    seen = [0] * (10**6+1)
    C = Counter(A)
    ans = 0
    if D == 0:
        return N - len(set(A))

    # for i in range(10**6+1):
    #     if seen[i]:
    #         continue
    #     x, y = 0, 0
    #     now = i
    #     while now <= 10**6 and C[now] > 0:
    #         x += C[now]
    #         seen[now] = 1
    #         now += D
    #         x, y = y, x
    #     ans += min(x, y)

    for i in range(10**6+1):
        if seen[i]:
            continue
        L = []
        now = i
        while now <= 10**6 and C[now] > 0:
            L.append(C[now])
            seen[now] = 1
            now += D
        if len(L) == 0:
            continue
        # print(L)
        # x個みて直前を採用してない/したときの最大採用
        dp = [[0, 0] for _ in range(len(L)+1)]
        for x, l in enumerate(L):
            dp[x+1][0] = max(dp[x][0], dp[x][1])
            dp[x+1][1] = dp[x][0] + l
        # print(dp)
        ans += sum(L) - max(dp[-1])
    return ans


def guchoku(N, D, A):
    for r in range(N+1):
        for B in combinations(A, N-r):
            ok = True
            for i in range(N-r):
                for j in range(i+1, N-r):
                    if abs(B[i]-B[j]) == D:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return r


if __name__ == "__main__":
    N, D = NMI()
    A = NLI()
    print(main(N, D, A))


    # from random import randint
    # for _ in range(1000):
    #     N = randint(1, 10)
    #     D = randint(0, 10)
    #     A = [randint(0, 10) for _ in range(N)]
    #     print(N, D, A)
    #     ans = main(N, D, A)
    #     gu = guchoku(N, D, A)
    #     print(ans)
    #     print(gu)
    #     assert ans == gu