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


def main():
    K, N = NMI()
    words = []
    for i in range(N):
        v, w = SI().split()
        d = len(w)
        words.append([v, w, d])

    ok_cases = []

    for x in product([1, 2, 3], repeat=K):
        ok = True
        for v, w, d in words:
            now = 0
            for n in v:
                n = int(n) - 1
                now += x[n]
            if d != now:
                ok = False
                break

        if ok:
            ok_cases.append(x)

    # print(ok_cases)

    for x in ok_cases:
        D = defaultdict(str)
        ok = True
        for v, w, d in words:
            idx = 0
            for n in v:
                n = int(n) - 1
                l = x[n]
                ww = w[idx: idx+l]
                idx += l

                if not D[n]:
                    D[n] = ww
                elif D[n] != ww:
                    ok = False

        if ok:
            for i in range(K):
                print(D[i])
            exit()


if __name__ == "__main__":
    main()
