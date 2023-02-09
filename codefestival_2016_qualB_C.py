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
    W, H = NMI()
    P = [NI() for _ in range(W)]
    Q = [NI() for _ in range(H)]
    X = [[p, i, 0] for i, p in enumerate(P)] + [[p, i, 1] for i, p in enumerate(Q)]
    # X.sort(key=lambda x: (x[0], -x[2]))
    X.sort()
    ans = 0
    w = W
    h = H
    for x, i, wh in X:
        if wh == 0:
            plus = x * (h+1)
            ans += plus
            w -= 1
        else:
            plus = x * (w+1)
            ans += plus
            h -= 1
        # print(ans, plus, x, w, h)
    print(ans)


if __name__ == "__main__":
    main()
