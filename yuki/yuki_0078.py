import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    S = SI()
    # i周終わったときの直前の購入回数
    B = [0] * 101
    total = 0
    now = 0
    for i in range(100):
        for s in S:
            if now == 0:
                B[i+1] += 1
            else:
                now -= 1
            if s == "0":
                pass
            elif s == "1":
                now += 1
            else:
                now += 2
            total += 1
            if total == K:
                print(sum(B))
                return

    if B[-1] == 0:
        print(sum(B))
        return

    x, r = divmod(K, N)
    ans = sum(B) + (x-100) * B[-1]

    for s in S[:r]:
        if now == 0:
            ans += 1
        else:
            now -= 1
        if s == "0":
            pass
        elif s == "1":
            now += 1
        else:
            now += 2

    print(ans)


if __name__ == "__main__":
    main()
