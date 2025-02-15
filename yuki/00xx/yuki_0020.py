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
    N, V, ow, oh = NMI()
    L = EI(N)
    ow, oh = ow-1, oh-1

    hq = []
    hq.append([-V, 0, 0, 0])
    seen = [[[-1] * N for _ in range(N)] for _ in range(2)]
    seen[0][0][0] = V

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]



    while hq:
        now_v, now_h, now_w, now_o = heappop(hq)
        now_v *= -1
        # print(now_v, now_h, now_w, now_o)
        if seen[now_o][now_h][now_w] > now_v:
            continue

        if now_h == oh and now_w == ow and now_o == 0:
            now_v *= 2
            now_o = 1
            seen[now_o][now_h][now_w] = now_v
        if now_h == N-1 and now_w == N-1:
            print("YES")
            # print(*seen, sep="\n")
            return

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_o = now_o

            if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                continue
            goto_v = now_v - L[goto_h][goto_w]
            if goto_v <= 0:
                continue
            if seen[goto_o][goto_h][goto_w] >= goto_v:
                continue

            heappush(hq, [-goto_v, goto_h, goto_w, goto_o])
            seen[goto_o][goto_h][goto_w] = goto_v


    print("NO")


if __name__ == "__main__":
    main()
