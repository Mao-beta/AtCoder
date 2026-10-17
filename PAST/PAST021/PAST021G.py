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
    N, K = NMI()
    ABI = [NLI() + [i+1] for i in range(N)]
    ABI.sort()
    ans = []
    for i in range(N-1):
        if ABI[i+1][0] - ABI[i][0] < ABI[i][1] * K:
            ans.append(ABI[i][2])
    ans.sort()
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
