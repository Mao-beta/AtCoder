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
    GD = EI(N)
    GD = [[g, d, i] for i, (g, d) in enumerate(GD, start=1)]
    GD.sort(key=lambda x: 30000*x[1] - x[0])
    g, d, i = GD[0]
    if (g - 30000 * d) * 6 >= 30000 * 100:
        print("YES")
        for _ in range(6):
            print(i)
    else:
        print("NO")



if __name__ == "__main__":
    main()
