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
    N = NI()
    AB = EI(N)
    Q = NI()
    XY = EI(Q)
    E = []
    for a, b in AB:
        E.append([a, 0, b, -1])
    for i, (x, y) in enumerate(XY):
        E.append([x, 1, y, i])
    E.sort()
    ans = [0] * Q
    C = [0] * (10**5+1)
    p = 0
    for X in E:
        if X[1] == 0:
            a, _, b, _ = X
            C[b] += 1
            p += 1
        else:
            x, _, y, i = X
            ans[i] = p - C[y]
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
