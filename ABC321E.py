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



def main():
    T = NI()
    for _ in range(T):
        N, X, K = NMI()
        if K >= 125:
            print(0)
            continue

        if K == 0:
            print(1)
            continue

        def down_k(x, k):
            # xからk階層子孫の左右
            l, r = x, x
            for i in range(k):
                l *= 2
                r *= 2
                r += 1
                if l > N:
                    return -1, -1

            return l, r

        ans = 0

        if (X >> K) > 0:
            ans += 1

        l, r = down_k(X, K)
        if l == -1:
            pass
        else:
            if r > N:
                r = N
            ans += r - l + 1

        for i in range(1, K+1):
            if (X >> i) <= 0:
                break
            now = X >> (i-1)
            now ^= 1
            rem = K - (i+1)

            if rem < 0:
                continue

            l, r = down_k(now, rem)
            if l == -1:
                continue
            else:
                if r > N:
                    r = N
                ans += r-l+1

        print(ans)



if __name__ == "__main__":
    main()
