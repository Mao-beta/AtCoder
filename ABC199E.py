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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, M = NMI()
    XYZ = EI(M)
    B = 1 << N
    dp = [0] * B
    dp[0] = 1
    order = []
    seen = [0] * B
    bins = [0] * B
    D = deque()
    D.append(0)
    while D:
        now = D.popleft()
        order.append(now)
        for i in range(N):
            if (now >> i) & 1:
                continue
            goto = now | (1<<i)
            if seen[goto]:
                continue
            D.append(goto)
            seen[goto] = 1
            bins[goto] = bins[now] + 1

    is_valid = [1] * B
    for case in order:
        b = bins[case]
        for x, y, z in XYZ:
            MASK = (1 << y) - 1
            if b > x:
                continue
            if bins[case & MASK] > z:
                is_valid[case] = 0
                break

    for case in order:
        for v in range(N):
            if (case >> v) & 1:
                continue
            nc = case | (1<<v)
            if is_valid[nc]:
                # print(bin(case)[2:].zfill(N), bin(nc)[2:].zfill(N))
                dp[nc] += dp[case]

    # print(dp)
    print(dp[-1])


if __name__ == "__main__":
    main()
