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
    N, M, K = NMI()
    A = NLI()

    def judge(X):
        # 全員がX以上になるときの回数がM以下か
        num = 0
        for a in A:
            if a >= X:
                continue
            k = (X-a+K-1)//K
            num += k
        return num <= M

    ok = 0
    ng = 10**18
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    ans = [a for a in A]
    m = M
    for i, a in enumerate(ans):
        if a >= ok:
            ans[i] = a
        else:
            k = (ok-a+K-1)//K
            b = k * K + a
            m -= k
            ans[i] = b

    hq = [[a, i] for i, a in enumerate(ans)]
    heapify(hq)
    for mi in range(m):
        a, i = heappop(hq)
        heappush(hq, [a+K, i])
        ans[i] += K

    print(*ans)


if __name__ == "__main__":
    main()
