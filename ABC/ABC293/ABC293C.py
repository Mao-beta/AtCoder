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
    H, W = NMI()
    A = EI(H)
    ans = 0
    for P in product([(0, 1), (1, 0)], repeat=H+W-2):
        ok = True
        S = set()
        S.add(A[0][0])
        h, w = 0, 0
        for dh, dw in P:
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W:
                a = A[nh][nw]
                if a in S:
                    ok = False
                    break
                S.add(a)
                h, w = nh, nw
            else:
                ok = False
                break

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
