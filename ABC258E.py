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
    N, Q, X = NMI()
    W = NLI()
    K = [NI() for _ in range(Q)]
    C = []
    S = sum(W)
    rem = X % S

    if rem == 0:
        for k in K:
            print(X // S * N)
        exit()

    else:
        que = deque()
        now = 0
        cnt = 0
        for w in W*2:
            now += w
            cnt += 1
            que.append(w)
            if now < rem:
                continue

            while cnt > 0 and now >= rem:
                # print(now, rem)
                rw = que.popleft()
                C.append(cnt + X // S * N)
                now -= rw
                cnt -= 1

        C = C[:N]

    G = [0]
    GS = {0}
    cum = [0]
    while True:
        now = G[-1]
        goto = C[now] + now
        goto %= N
        cum.append(cum[-1] + C[now])
        G.append(goto)
        if goto in GS:
            start = G.index(goto)
            end = len(G) - 1
            break
        GS.add(goto)

    # print(C)
    # print(G)
    # print(GS)
    # print(cum)
    # print(start, end)
    gap = cum[end] - cum[start]
    for k in K:
        k -= 1
        if k <= start:
            print(C[G[k]])
            continue
        k -= start
        k %= end - start
        x = start + k
        # print(x)
        print(C[G[x]])


if __name__ == "__main__":
    main()
