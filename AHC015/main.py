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
    A = NLI() + [0]
    C = Counter(A)
    t = C.most_common()[0][0]
    for i in range(100):
        a = A[i+1]
        p = A[i]
        x = NI()

        if a == t:
            print("F")
        else:
            if p == t:
                print("B")
            elif a == t % 3 + 1:
                print("R")
            else:
                print("L")

        sys.stdout.flush()


import random

def _main():
    A = NLI() + [0]
    C = Counter(A)
    t = C.most_common()[0][0]
    t2 = C.most_common()[1][0]

    for i in range(100):
        a = A[i+1]
        p = A[i]
        x = NI()

        if a == t:
            print("F")
        else:
            if p == t:
                print("B")

            else:
                if a == t2:
                    print("L")
                else:
                    if p == t2:
                        print("R")
                    else:
                        print("B")


        sys.stdout.flush()


if __name__ == "__main__":
    _main()
