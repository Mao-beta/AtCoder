import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


from random import randint
import time

def main():
    start = time.time()
    N, Pa, Pb = SMI()
    N = int(N)
    Pa += "0" * (5 - len(Pa))
    Pb += "0" * (5 - len(Pb))
    Pa = int(Pa.replace(".", ""))
    Pb = int(Pb.replace(".", ""))
    A = NLI()
    B = NLI()

    def trial():
        HA = A[:]
        HB = B[:]
        sa = 0
        sb = 0
        for _ in range(N):
            HA.sort()
            HB.sort()

            ar = randint(1, 1000)
            if len(HA) == 1 or ar <= Pa:
                a = HA[0]
                HA.pop(0)
            else:
                idx = randint(1, len(HA)-1)
                a = HA[idx]
                HA.pop(idx)

            br = randint(1, 1000)
            if len(HB) == 1 or br <= Pb:
                b = HB[0]
                HB.pop(0)
            else:
                idx = randint(1, len(HB) - 1)
                b = HB[idx]
                HB.pop(idx)

            if a > b:
                sa += a+b
            else:
                sb += a+b

        return sa > sb

    total = 0
    win = 0
    while time.time() - start < 2.9:
        total += 1
        win += int(trial())

    print(win / total)


if __name__ == "__main__":
    main()
