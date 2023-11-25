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


def main():
    Ha, Wa = NMI()
    A = [SI() for _ in range(Ha)]
    Hb, Wb = NMI()
    B = [SI() for _ in range(Hb)]
    Hx, Wx = NMI()
    X = [SI() for _ in range(Hx)]

    def extract(G, H, W):
        res = set()
        for h in range(H):
            for w in range(W):
                if G[h][w] == "#":
                    res.add((h, w))
        return res

    Ahw = extract(A, Ha, Wa)
    Bhw = extract(B, Hb, Wb)
    Xhw = extract(X, Hx, Wx)

    def move(Ghw, gh, gw):
        res = set()
        for h, w in Ghw:
            res.add((h+gh, w+gw))
        return res

    def normalize(Ghw):
        res = sorted(list(Ghw))
        sh, sw = res[0]
        res = [(h-sh, w-sw) for h, w in res]
        return res

    Xhw = normalize(Xhw)

    for gh in range(-30, 31):
        for gw in range(-30, 31):
            Am = move(Ahw, gh, gw)
            AB = Am | Bhw
            AB = normalize(AB)
            if Xhw == AB:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
