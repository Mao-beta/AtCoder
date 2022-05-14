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
    N, a = NMI()
    K = NI()
    B = NLI()
    B = [x-1 for x in B]
    a -= 1

    D = {a: 0}
    L = [a]
    now = a
    num = 0
    start = -1
    end = -1
    while True:
        num += 1
        goto = B[now]
        if goto in D:
            start = D[goto]
            end = num
            break
        else:
            D[goto] = num
            L.append(goto)
            now = goto

    loop = end - start

    if K < end:
        print(L[K]+1)
        exit()

    K -= start
    K %= loop
    K += start
    print(L[K]+1)


if __name__ == "__main__":
    main()
