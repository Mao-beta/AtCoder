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
    N = NI()
    S = [SI() for _ in range(N)]
    sh, sw = 0, 0
    for h in range(N):
        for w in range(N):
            if S[h][w] == "S":
                sh, sw = h, w

    def solve(k):
        start = (sh, sw, 0)

        queue = deque()
        queue.append(start)
        D = [[-1] * N for _ in range(N)]
        D[start[0]][start[1]] = 0

        DH = [0, 0, 1, -1]
        DW = [1, -1, 0, 0]

        seen = set()
        seen.add((sh, sw))

        while queue:
            now_h, now_w, now_step = queue.popleft()
            if S[now_h][now_w] == "G":
                return now_step

            for dh, dw in zip(DH, DW):
                goto_step = now_step + 1
                ok = True
                for ki in range(1, k+1):
                    goto_h = now_h + dh * ki
                    goto_w = now_w + dw * ki

                    if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                        ok = False
                        break
                    if S[goto_h][goto_w] == "X":
                        ok = False
                        break
                    if ki == k and (goto_h, goto_w) in seen:
                        ok = False
                        break
                if ok:
                    goto_h = now_h + dh * k
                    goto_w = now_w + dw * k
                    queue.append((goto_h, goto_w, goto_step))
                    seen.add((goto_h, goto_w))

        return -1


    for k in range(1, N):
        res = solve(k)
        print(res)


if __name__ == "__main__":
    main()
