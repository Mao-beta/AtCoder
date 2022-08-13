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
    PtoMaxE = defaultdict(int)
    PtoIsOnly = defaultdict(lambda: True)

    if N == 1:
        print(1)
        exit()

    A = []
    for i in range(N):
        m = NI()
        a = []
        for j in range(m):
            p, e = NMI()
            a.append([p, e])
            if PtoMaxE[p] == e:
                PtoIsOnly[p] = False
            elif PtoMaxE[p] < e:
                PtoMaxE[p] = e
                PtoIsOnly[p] = True

        A.append(a)

    # print(PtoMaxE)
    ans = 0
    base = 0
    for a in A:
        flag = True

        for p, e in a:
            if PtoMaxE[p] == e and PtoIsOnly[p]:
                ans += 1
                flag = False
                break

        if flag:
            base = 1

    print(ans + base)


if __name__ == "__main__":
    main()
