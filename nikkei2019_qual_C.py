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
    AB = [NLI() for _ in range(N)]
    D = [[a+b, a, b] for a, b in AB]
    D.sort(reverse=True)
    ans = 0
    for i, (ab, a, b) in enumerate(D):
        ans += [a, b][i%2] * (-1)**(i%2)
    print(ans)


if __name__ == "__main__":
    main()