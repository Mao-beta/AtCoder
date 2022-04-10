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
    L, R = NMI()
    R += 1
    M = NI()
    D = [1]
    S = {1: 0}
    start = 0
    end = 1
    for i in range(1, 10**6):
        x = D[-1]*5 % (10**M)
        if x not in S:
            D.append(x)
            S[x] = i
        else:
            start = S[x]
            end = i
            break


    def f(x):
        res = 0
        while x > 0:
            res += x % 10
            x //= 10
        return res

    D = [f(x) for x in D]

    def g(K):
        if K <= end:
            return sum(D[:K])

        loop = sum(D[start: end])
        T = end - start
        res = sum(D[:start])
        K -= start
        res += (K // T) * loop
        K %= T
        res += sum(D[start:start+K])
        return res


    print(g(R) - g(L))


if __name__ == "__main__":
    main()
