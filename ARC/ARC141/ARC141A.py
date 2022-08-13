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


def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def solve(N):
    L = len(N)

    D = divisors(L)
    ans = 0
    for d in D:
        if d == L:
            continue
        tmp = int("9" * d)
        tmp_s = "9" * d

        minus = False
        for l in range(0, L - d + 1, d):
            r = l + d
            # print("lr", l, r)
            if l == 0:
                tmp = int(N[l:r])
                tmp_s = N[l:r]

            elif tmp < int(N[l:r]):
                break

            elif tmp > int(N[l:r]) and not minus:
                tmp -= 1
                tmp_s = str(tmp)
                minus = True
                if tmp < 0:
                    tmp = 0
                    tmp_s = "0"
                break
            # print(tmp, tmp_s)

        ans = max(ans, int(tmp_s * (L // d)))
        # print("a", ans)

    L -= 1
    D = divisors(L)
    N = "9" * L
    for d in D:
        if d == L:
            continue
        tmp = int("9" * d)
        tmp_s = "9" * d

        minus = False
        for l in range(0, L - d + 1, d):
            r = l + d
            # print("lr", l, r)
            if l == 0:
                tmp = int(N[l:r])
                tmp_s = N[l:r]

            elif tmp < int(N[l:r]):
                break

            elif tmp > int(N[l:r]) and not minus:
                tmp -= 1
                tmp_s = str(tmp)
                minus = True
                if tmp < 0:
                    tmp = 0
                    tmp_s = "0"
                break
            # print(tmp, tmp_s)

        ans = max(ans, int(tmp_s * (L // d)))

    return ans


def main():
    T = NI()
    for _ in range(T):
        N = SI()
        print(solve(N))

    # for N in range(11, 1000):
    #     print(N, solve(str(N)))


if __name__ == "__main__":
    main()
