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
EI = lambda m: [NLI() for _ in range(m)]


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    H, W = NMI()
    A = [SI() for _ in range(H)]
    Q = NI()
    h, w = 0, 0
    for _ in range(Q):
        a, b = NMI()
        if h < a and w < b:
            h, w = a-1-h, b-1-w
        elif h >= a and w < b:
            h, w = a+H-1-h, b-1-w
        elif h < a and w >= b:
            h, w = a-1-h, b+W-1-w
        else:
            h, w = a+H-1-h, b+W-1-w

    ans = [[""] * W for _ in range(H)]
    if Q % 2 == 0:
        for ah in range(H):
            for aw in range(W):
                sh = (ah + h) % H
                sw = (aw + w) % W
                ans[sh][sw] = A[ah][aw]

    else:
        for ah in range(H):
            for aw in range(W):
                sh = (-ah + h) % H
                sw = (-aw + w) % W
                ans[sh][sw] = A[ah][aw]

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
