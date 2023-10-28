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


def main():
    N = NI()
    R = SI()
    C = SI()

    As = set()
    Bs = set()
    Cs = set()
    for P in permutations("ABC"+"."*(N-3), N):
        for x in P:
            if x == ".":
                continue
            if x == "A":
                As.add(P)
                break
            elif x == "B":
                Bs.add(P)
                break
            else:
                Cs.add(P)
                break

    X = []
    for r in R:
        if r == "A":
            X.append(As)
        elif r == "B":
            X.append(Bs)
        else:
            X.append(Cs)

    for P in product(*X):
        T = list(zip(*P))
        ok = True
        for c, col in zip(C, T):
            if c == "A" and col in As:
                pass
            elif c == "B" and col in Bs:
                pass
            elif c == "C" and col in Cs:
                pass
            else:
                ok = False
        if ok:
            print("Yes")
            for row in P:
                print("".join(row))
            return

    print("No")


if __name__ == "__main__":
    main()
