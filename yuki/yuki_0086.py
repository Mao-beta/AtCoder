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
    A = [SI() for _ in range(H)]
    total = sum(a.count(".") for a in A)
    # DRUL
    DH = [1, 0, -1, 0]
    DW = [0, 1, 0, -1]

    INF = 10**5
    for sh in range(H):
        for sw in range(W):
            if A[sh][sw] == "#":
                continue
            steps = [[-INF]*W for _ in range(H)]
            h, w = sh, sw
            R = 0
            d = 0
            steps[sh][sw] = 1
            while True:
                # print(h, w, d)
                rd = (d-1) % 4
                nrh, nrw = h+DH[rd], w+DW[rd]
                if 0 <= nrh < H and 0 <= nrw < W:
                    if A[nrh][nrw] == ".":
                        if R == 1:
                            print("NO")
                            return
                        else:
                            R += 1
                            d = rd

                nh, nw = h+DH[d], w+DW[d]
                if 0 <= nh < H and 0 <= nw < W:
                    if A[nh][nw] == "#":
                        d = (d+1) % 4
                else:
                    d = (d+1) % 4

                nh, nw = h+DH[d], w+DW[d]
                # print(nh, nw)
                if 0 <= nh < H and 0 <= nw < W:
                    if nh == sh and nw == sw:
                        # print(*steps, sep="\n")

                        if steps[h][w] == total:
                            print("YES")
                            return
                        else:
                            print("NO")
                            return
                    elif steps[nh][nw] >= 0:
                        print("NO")
                        return
                    else:
                        steps[nh][nw] = steps[h][w] + 1
                        h = nh
                        w = nw

                else:
                    print("NO")
                    return


if __name__ == "__main__":
    main()
