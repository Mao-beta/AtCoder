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
    ans = [K]
    U = 0
    for n in range(N):
        tmp = []
        # print(ans)
        for i in range(1<<n):
            # print(i)
            a = ans[i]
            tmp.append(a//2)
            tmp.append(a - a//2)
        U = max(max(tmp) - min(tmp), U)
        ans = tmp[:]
    print(U)
    print(*ans)


if __name__ == "__main__":
    main()
