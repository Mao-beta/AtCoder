import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, K = NMI()
    A = NLI() + [0]
    # stackに単調増加(h, pos)を持つ
    D = [[0, -1]]
    # 横に伸びる層におけるwidthとheightを補完
    WH = []
    for i, a in enumerate(A):
        if D[-1][0] < a:
            D.append([a, i])
        else:
            while D[-2][0] > a:
                h = D[-1][0] - D[-2][0]
                w = i - D[-1][1]
                WH.append([w, h])
                D.pop()
            h = D[-1][0] - a
            w = i - D[-1][1]
            WH.append([w, h])
            D[-1][0] = a

    WH.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * 4 + 1
        if i < N-1:
            ans -= min(A[i], A[i+1]) * 2

    for w, h in WH:
        if K >= w * h:
            K -= w * h
            ans -= w * h * 2 + h * 2
        else:
            x, r = divmod(K, w)
            ans -= w * x * 2 + x * 2
            ans -= r * 2
            break
    print(ans)


if __name__ == "__main__":
    main()
