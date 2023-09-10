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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    C = EI(3)

    X = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
         [0, 3, 6], [1, 4, 7], [2, 5, 8],
         [0, 4, 8], [2, 4, 6]]

    ans = 0
    for P in permutations(range(9)):
        cs = []
        IDX = [[p, i] for i, p in enumerate(P)]
        IDX.sort()
        IDX = [i for p, i in IDX]
        # print(P, IDX)
        for p in P:
            h, w = divmod(p, 3)
            cs.append(C[h][w])

        gakkari = False
        for abc in X:
            tmp = []
            for x in abc:
                # print(x)
                tmp.append([IDX[x], cs[IDX[x]]])
            tmp.sort()
            if tmp[0][1] == tmp[1][1]:
                gakkari = True

        if not gakkari:
            ans += 1

    print(ans / math.factorial(9))


if __name__ == "__main__":
    main()
