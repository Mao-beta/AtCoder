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
    H, W = NMI()
    S = [SI() for _ in range(H)]
    B = []
    D = {}
    cnt = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                B.append((h, w))
                D[(h, w)] = cnt
                cnt += 1
    if len(B) % 2:
        print("NO")
        return

    for i in range(1, len(B)):
        used = [0] * len(B)
        hi, wi = B[i]
        h0, w0 = B[0]
        gh, gw = hi-h0, wi-w0
        ok = True
        for j in range(len(B)):
            if used[j]:
                continue
            used[j] = 1
            h, w = B[j]
            nh, nw = h+gh, w+gw
            if (nh, nw) in D:
                used[D[(nh, nw)]] = 1
            else:
                ok = False
                break
        # print(used)
        if ok:
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    main()
