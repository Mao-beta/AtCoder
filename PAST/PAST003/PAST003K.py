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
    N, Q = NMI()
    FTX = [NLI() for _ in range(Q)]

    # コンテナは正、机は負の番号
    # D[i] 物体iの下のものの番号
    # ない場合は0
    D = [0] * (2*N+1)
    top = [0] * (N+1)

    for i in range(1, N+1):
        D[i] = -i
        top[i] = i

    for f, t, x in FTX:
        f_top = top[f]
        t_top = top[t]

        top[t] = f_top
        d = D[x]
        top[f] = d
        D[x] = t_top

    ans = [0] * (N+1)
    for i in range(1, N+1):
        t = top[i]
        while t > 0:
            ans[t] = i
            t = D[t]

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
