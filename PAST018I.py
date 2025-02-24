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
    Q = NI()
    ans = []
    row = []
    tmp = []
    w = 1
    for _ in range(Q):
        qi, *c = SMI()
        if qi == "1":
            tmp.append(c[0])
            w += 1
        elif qi == "2":
            row += tmp[:][::-1]
            tmp = []
            w = 1
        else:
            row += tmp[:][::-1]
            ans.append(row[:])
            tmp = []
            row = []
            w = 1
        # print(ans, w)
    row += tmp[:][::-1]
    ans.append(row[:])
    print(len(ans), w)
    for row in ans:
        print("#", "".join(row[::-1]))


if __name__ == "__main__":
    main()
