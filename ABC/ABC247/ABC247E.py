import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    N, X, Y = NMI()
    A = NLI()

    if X == Y:
        cnt = 0
        ans = 0
        for a in A:
            if a == X:
                cnt += 1
            else:
                ans += (cnt+1) * cnt // 2
                cnt = 0
        ans += (cnt + 1) * cnt // 2
        print(ans)
        exit()


    p, m, M, mM = 0, 0, 0, 0
    ans = 0
    for a in A:
        if a == X:
            p, m, M, mM = 0, 0, p+M+1, mM+m
            ans += mM
        elif a == Y:
            p, m, M, mM = 0, p+m+1, 0, mM+M
            ans += mM
        elif Y < a < X:
            p, m, M, mM = p+1, m, M, mM
            ans += mM
        else:
            p, m, M, mM = 0, 0, 0, 0

    print(ans)



if __name__ == "__main__":
    main()
