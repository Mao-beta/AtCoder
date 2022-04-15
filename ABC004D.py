import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def calc(center, l, r):
    l -= center
    r -= center
    r -= 1

    if l * r <= 0:
        l = abs(l)
        return r * (r+1) // 2 + l * (l+1) // 2

    if r < 0:
        l, r = -r, -l

    return (l+r) * (r-l+1) // 2


def main():
    R, G, B = NMI()
    INF = 10**10
    ans = INF
    for gl in range(-51-G, 52):
        res = 0
        gr = gl + G
        res += calc(0, gl, gr)
        # print(gl, gr)
        # print("G", res)

        if -100 + R//2 <= gl:
            res += calc(-100, -100 + R//2 - R + 1, -100 + R//2 + 1)
        else:
            res += calc(-100, gl-R, gl)
        # print("GR", res)

        if 100 - B//2 >= gr:
            res += calc(100, 100 - B//2, 100 - B//2 + B)
        else:
            res += calc(100, gr, gr+B)


        ans = min(ans, res)

        # print(res)

    print(ans)


if __name__ == "__main__":
    main()
