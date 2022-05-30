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
    A = NLI()
    B = NLI()
    G = [a-b for a, b in zip(A, B)]

    ans = 0
    minus = 0
    plus = []
    for g in G:
        if g < 0:
            minus += g
            ans += 1
        else:
            plus.append(g)

    plus.sort(reverse=True)
    plus = [0] + list(accumulate(plus))

    # print(minus)
    # print(plus)
    # print(ans)
    ans += bisect.bisect_left(plus, -minus)
    print(ans if ans <= N else -1)


if __name__ == "__main__":
    main()
