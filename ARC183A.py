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
    if N == 1:
        ans = [N] * K
        print(*ans)
        return

    if N % 2 == 0:
        ans = [N//2]
        for n in range(N, 0, -1):
            ans += [n] * K
            if n == N//2:
                ans.pop()
        print(*ans)

    else:
        ans = [(N+1)//2] * K
        ans += [(N+1)//2-1]
        for n in range(N, 0, -1):
            if n == (N+1)//2:
                continue
            ans += [n] * K
            if n == (N+1)//2-1:
                ans.pop()

        print(*ans)



if __name__ == "__main__":
    main()
