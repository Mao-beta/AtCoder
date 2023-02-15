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


def get_msb(v):
    # v以下の最大の2べき
    v |= (v >> 1)
    v |= (v >> 2)
    v |= (v >> 4)
    v |= (v >> 8)
    v |= (v >> 16)
    v |= (v >> 32)
    return 1 << (bin(v).count("1") - 1)


def main():
    N = NI()
    A = NLI()
    A.sort(reverse=True)
    C = Counter(A)
    ans = 0
    for a in A:
        if C[a] <= 0:
            continue
        C[a] -= 1
        msb = get_msb(a)
        target = msb * 2 - a
        if C[target] > 0:
            ans += 1
            C[target] -= 1
    print(ans)


if __name__ == "__main__":
    main()
