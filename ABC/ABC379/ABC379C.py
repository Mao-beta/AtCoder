import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, M = NMI()
    X = NLI()
    A = NLI()
    if sum(A) != N:
        print(-1)
        return
    XA = sorted([[x, a] for x, a in zip(X, A)], reverse=True)
    ans = 0
    now = N
    for x, a in XA:
        if now-x-(a-1) < 0:
            print(-1)
            return
        ans += (now-x + now-x-(a-1)) * a // 2
        now -= a
    print(ans)


if __name__ == "__main__":
    main()
