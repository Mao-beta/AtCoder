import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    INF = 10**15
    for _ in range(T):
        N, K = NMI()
        L = NLI()
        R = NLI()
        now = 0
        hq = []
        ans = INF
        for i in range(N):
            l, r = L[i], R[i]
            n = r-l+1
            rem = K - now
            if rem <= 0:
                break
            # n個塗ってもKに達しないとき
            if rem > n:
                heappush(hq, n)
                now += n
                continue

            # この区間だけでKある
            if n >= K:
                ans = min(ans, l+K-1 + 2)
                break

            # print(l, r, now, hq)
            # n個以下塗ってKに達するとき
            # この区間で終える(最後にlからrem個塗る→l+rem-1)
            ans = min(ans, l+rem-1 + (len(hq)+1) * 2)
            tmp = []
            while hq and now - hq[0] + n >= K and hq[0] < n:
                x = heappop(hq)
                rem += x
                now -= x
                tmp.append(x)
                ans = min(ans, l+rem-1 + (len(hq)+1) * 2)

            tmp.append(n)
            for t in tmp:
                now += t
                heappush(hq, t)

            # 余剰を捨てる
            while hq and now >= K:
                x = heappop(hq)
                now -= x

        print(-1 if ans == INF else ans)


if __name__ == "__main__":
    main()
