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


def main(N, L, A):
    if L == 1:
        print("Yes")
        exit()

    idx = 1
    C = [0] * L
    for a in A:
        # print(idx, C)
        if a == 1:
            if idx > L-1:
                continue
            else:
                C[idx] = 1
                idx += 2
        else:
            if idx == L-1:
                C[idx] = 1
                C[idx-1] = 1
                idx += 2
            elif idx > L-1:
                print("No")
                exit()
            else:
                C[idx] = 1
                C[idx+1] = 1
                idx += 3

    print("Yes")


if __name__ == "__main__":
    N, L = NMI()
    A = NLI()
    main(N, L, A)
