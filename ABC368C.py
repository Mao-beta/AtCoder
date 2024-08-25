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
    # 1 2 3 3 3
    # 1 2 2 2 3
    # 1 1 1 2 3
    N = NI()
    H = NLI()
    T = 0
    for h in H:
        if h % 5 == 0:
            T += h // 5 * 3
            continue

        if T % 3 == 0:
            T += h // 5 * 3
            h %= 5
            if h == 0:
                h = 5
            if h == 1:
                T += 1
            elif h == 2:
                T += 2
            else:
                T += 3

        elif T % 3 == 1:
            T += h // 5 * 3
            h %= 5
            if h == 0:
                h = 5
            if h == 1:
                T += 1
            elif 2 <= h <= 4:
                T += 2
            else:
                T += 3

        else:
            T += h // 5 * 3
            h %= 5
            if h == 0:
                h = 5
            if h <= 3:
                T += 1
            elif h == 4:
                T += 2
            else:
                T += 3
        # print(T)

    print(T)


if __name__ == "__main__":
    main()

    # for h_ in range(1, 18):
    #     h = h_
    #     T = 0
    #     while h > 0:
    #         T += 1
    #         if T % 3 == 0:
    #             h -= 3
    #         else:
    #             h -= 1
    #     print(h_, T)
