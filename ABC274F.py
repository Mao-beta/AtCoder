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
    N, A = NMI()
    WXV = [tuple(NMI()) for _ in range(N)]
    ans = 0

    for ib, (wb, xb, vb) in enumerate(WXV):
        F = [(w, x-xb, v-vb) for w, x, v in WXV]
        T = [(0, -1)]
        tmp = wb

        for i, (w, x, v) in enumerate(F):
            if i == ib: continue
            if v == 0:
                if 0 <= x <= A:
                    tmp += w
            else:
                T.append((int(-x*10**9/v), i))
                T.append((int((A-x)*10**9/v), i))
        T.sort()
        # print(T)
        S = set()
        for t, i in T:
            if i == -1:
                ans = max(ans, tmp)
                continue

            if i not in S:
                S.add(i)
                tmp += F[i][0]
            else:
                S.discard(i)
                tmp -= F[i][0]

            # print(tmp)

            if t >= 0:
                ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
