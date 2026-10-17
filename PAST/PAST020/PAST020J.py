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
    N = NI()
    S = [[int(s=="#") for s in SI()] for _ in range(N)]

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    ans = 0

    que = deque()
    for h in range(N):
        for w in range(N):
            if S[h][w] == "#":
                continue
            cnt = 0
            for dh, dw in zip(DH, DW):
                nh = h + dh
                nw = w + dw
                if nh < 0 or nh >= N or nw < 0 or nw >= N:
                    continue
                if S[nh][nw]:
                    cnt += 1
            if cnt > 2:
                que.append([h, w])

    while que:
        now_h, now_w = que.popleft()
        if S[now_h][now_w]:
            continue
        cnt = 0
        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                continue
            if S[goto_h][goto_w]:
                cnt += 1
        if cnt > 2:
            ans += 1
            # print(now_h, now_w)
            S[now_h][now_w] = 1

            for dh, dw in zip(DH, DW):
                goto_h = now_h + dh
                goto_w = now_w + dw
                if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                    continue
                if S[goto_h][goto_w]:
                    continue
                que.append([goto_h, goto_w])

    print(ans)


if __name__ == "__main__":
    main()
