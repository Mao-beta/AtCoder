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
    N = NI()
    XY = EI(N)
    D = Counter()
    D2 = Counter()
    ans = 0
    for i, (x1, y1) in enumerate(XY):
        for j, (x2, y2) in enumerate(XY):
            if i >= j:
                continue
            x = x2 - x1
            y = y2 - y1
            if x == 0:
                D[(0, 1)] += 1
                D2[(0, 1, abs(y))] += 1
            elif y == 0:
                D[(1, 0)] += 1
                D2[(1, 0, abs(x))] += 1
            else:
                g = math.gcd(x, y)
                x //= g
                y //= g
                if x < 0:
                    x, y = -x, -y
                D[(x, y)] += 1
                D2[(x, y, abs(x) * g)] += 1
    for V, k in D.items():
        # print(V, k)
        ans += k * (k-1) // 2
    over = 0
    for V, k in D2.items():
        # print(V, k)
        over += k * (k-1) // 2
    print(ans - over // 2)


if __name__ == "__main__":
    main()
