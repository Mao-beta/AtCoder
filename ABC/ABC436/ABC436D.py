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
    H, W = NMI()
    HW = H*W
    S = [SI() for _ in range(H)]
    G = [[] for _ in range(HW+26)]

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    for h in range(H):
        for w in range(W):
            s = S[h][w]
            hw = h*W+w
            if s == "#":
                continue
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if S[nh][nw] == "#":
                    continue
                nhw = nh*W+nw
                G[hw].append(nhw)

            if ord(s) >= ord("a"):
                ns = HW + ord(s) - ord("a")
                G[hw].append(ns)
                G[ns].append(hw)

    steps = [-1] * (HW+26)
    que = deque()
    que.append(0)
    steps[0] = 0
    # print(G)
    while que:
        now = que.popleft()
        step = steps[now]
        # print(divmod(now, W), now, step, que)
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            if goto >= HW:
                que.appendleft(goto)
                steps[goto] = step
            else:
                que.append(goto)
                steps[goto] = step + 1

        # print(steps)

    print(steps[HW-1])


if __name__ == "__main__":
    main()
