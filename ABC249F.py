import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    N, K = NMI()
    TY = [[1, 0]] + [NLI() for _ in range(N)]
    ignores = []
    total = 0
    INF = 10**18
    ans = -INF

    for t, y in TY[::-1]:
        if t == 1:
            ans = max(ans, y + total)
            if K > 0:
                K -= 1
            else:
                break
        else:
            if y < 0:
                heappush(ignores, -y)
            else:
                total += y

        while ignores and len(ignores) > K:
            x = -heappop(ignores)
            total += x

    print(ans)


if __name__ == "__main__":
    main()
