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


def main():
    p1, q1, r1, s1, u1, v1 = NMI()
    p2, q2, r2, s2, u2, v2 = NMI()
    # 相対速度化
    u2 -= u1
    v2 -= v1
    u1, v1 = 0, 0
    # 相対速度が正になるように各軸を反転
    if u2 < 0:
        p1, r1, u1 = -r1, -p1, -u1
        p2, r2, u2 = -r2, -p2, -u2
    if v2 < 0:
        q1, s1, v1 = -s1, -q1, -v1
        q2, s2, v2 = -s2, -q2, -v2
    # A左下が原点になるように平行移動
    p2 -= p1
    q2 -= q1
    r2 -= p1
    s2 -= q1
    r1 -= p1
    s1 -= q1
    p1, q1 = 0, 0

    # print(p1, q1, r1, s1)
    # print(p2, q2, r2, s2)
    # print(u1, v1, u2, v2)

    if p2 >= r1:
        print(0)
        return
    if q2 >= s1:
        print(0)
        return

    if u2 == 0 and r2 <= p1:
        print(0)
        return
    if v2 == 0 and s2 <= q1:
        print(0)
        return

    # t == (p1 - r2) / u2
    if u2 != 0:
        txl = (p1 - r2) / u2
        txr = (r1 - p2) / u2
    else:
        txl = 0
        txr = float("inf")

    if v2 != 0:
        tyl = (q1 - s2) / v2
        tyr = (s1 - q2) / v2
    else:
        tyl = 0
        tyr = float("inf")

    txl = max(txl, 0)
    tyl = max(tyl, 0)
    txr = max(txr, 0)
    tyr = max(tyr, 0)
    # print(txl, txr, tyl, tyr)
    l = max(txl, tyl)
    r = min(txr, tyr)
    print(max(0, r-l))


if __name__ == "__main__":
    main()
