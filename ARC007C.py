import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def main(C):
    N = len(C)
    B = 1<<N
    x = 0
    for i, c in enumerate(C):
        if c == "o":
            x += 1<<i
    x = x + (x << N)
    mask = B - 1
    ans = N
    for case in range(B):
        tmp = 0
        b = 0
        for i in range(N):
            if (case >> i) & 1:
                tmp |= x << i
                b += 1
        while tmp > 0:
            if tmp % B == mask:
                # print(bin(case), bin(tmp))
                ans = min(ans, b)
            tmp >>= 1
    print(ans)


if __name__ == "__main__":
    C = SI()
    main(C)
    # for C in product("ox", repeat=4):
    #     if "o" not in C:
    #         continue
    #     print("".join(C))
    #     main(C)
