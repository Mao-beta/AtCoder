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
    Q = NI()
    D = deque()
    for _ in range(Q):
        q, *t = NLI()
        if q == 1:
            x, c = t
            D.append((x, c))
        else:
            c = t[0]
            ans = 0
            while c > 0:
                a, k = D.popleft()
                if k > c:
                    D.appendleft((a, k-c))
                    ans += a * c
                    c = 0
                else:
                    c -= k
                    ans += a * k
            print(ans)


if __name__ == "__main__":
    main()
