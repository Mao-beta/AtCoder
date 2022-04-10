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
    N, K = NMI()
    A = NLI()
    L = []
    ans = 10**10
    for i, a in enumerate(A):
        if i < K:
            L.append((a, i))
            if i == K-1:
                L.sort(key=lambda x: (x[0], -x[1]))
                L = deque(L)
        else:
            # print(L, i, a)
            # print(L[0][0])
            while L and L[0][0] < a:
                b, x = L.popleft()
                ans = min(ans, i-x)
            # print(ans)

    print(ans if ans < 10**10 else -1)


if __name__ == "__main__":
    main()
