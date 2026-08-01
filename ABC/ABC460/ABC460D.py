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
    S = [SI() for _ in range(H)]

    DH = [0, 0, 1, -1, 1, 1, -1, -1]
    DW = [1, -1, 0, 0, 1, -1, 1, -1]

    dp = [[-1]*W for _ in range(H)]
    que = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                ok = False
                for dh, dw in zip(DH, DW):
                    nh, nw = h + dh, w + dw
                    if nh < 0 or nw < 0 or nh >= H or nw >= W:
                        continue
                    if S[nh][nw] == "#":
                        ok = True
                if ok:
                    dp[h][w] = 0
                    que.append((h, w))
    if len(que) == 0:
        for i in range(H):
            print("."*W)
        return

    while que:
        h, w = que.popleft()
        d = dp[h][w]
        for dh, dw in zip(DH, DW):
            nh, nw = h + dh, w + dw
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if dp[nh][nw] != -1:
                continue
            dp[nh][nw] = d+1
            que.append((nh, nw))
    # print(*dp, sep="\n")
    for row in dp:
        ans = ["." if d % 2 == 0 else "#" for d in row]
        print("".join(ans))


if __name__ == "__main__":
    main()
