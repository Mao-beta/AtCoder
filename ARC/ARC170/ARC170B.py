import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def main():
    N = NI()
    A = NLI()
    C = Counter()
    dp = [[0]*11 for _ in range(11)]
    D = deque()
    ans = (N+1) * N // 2
    r = 0
    for l in range(N):
        # のばす
        while r < N:
            a = A[r]
            ok = True
            for p in range(1, 11):
                for q in range(1, 11):
                    if p + a != 2 * q:
                        continue
                    if dp[p][q] > 0:
                        ok = False
            if ok:
                D.append(a)
                for p in range(1, 11):
                    dp[p][a] += C[p]
                C[a] += 1
                r += 1
            else:
                break
        ans -= r-l

        if D:
            x = D.popleft()
            C[x] -= 1
            for q in range(1, 11):
                dp[x][q] -= C[q]

    print(ans)



if __name__ == "__main__":
    main()
