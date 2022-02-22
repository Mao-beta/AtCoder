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


def main():
    N = NI()
    A = NLI()
    D = deque()
    num = 0
    for a in A:
        if not D:
            D.append([a, 1])
            num += 1
        else:
            x, k = D.pop()
            if x == a:
                k += 1
                if k < x:
                    D.append([x, k])
                    num += 1
                else:
                    num -= k-1
            else:
                D.append([x, k])
                D.append([a, 1])
                num += 1
        print(num)


if __name__ == "__main__":
    main()
