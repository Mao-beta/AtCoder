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


def grundy_tactics(N, L, R):
    G = [0] * (N+1)

    for x in range(N+1):
        if x < L:
            continue

        # x枚のカードが連続である状態
        S = set()
        for l in range(x-L+1):
            r = l + L
            g = G[l] ^ G[x-r]
            S.add(g)

        for g in range(N+1):
            if g not in S:
                G[x] = g
                break

    # print(G)

    D = [(1, N+1)]
    g_now = G[N]

    if g_now > 0:
        print("First")
        sys.stdout.flush()

        ok = False
        for i, (l, r) in enumerate(D):
            if r - l < L:
                continue
            g_else = g_now ^ G[r-l]
            for x in range(l, r-L+1):
                if g_else ^ G[x-l] ^ G[r-(x+L)] == 0:
                    print(x, L)
                    sys.stdout.flush()
                    g_now = g_else ^ G[x-l] ^ G[r-(x+L)]
                    D.pop(i)
                    if x-l > 0:
                        D.append((l, x))
                    if r-(x+L) > 0:
                        D.append((x+L, r))
                    ok = True
                    break
            if ok:
                break

    else:
        print("Second")
        sys.stdout.flush()

    while True:
        a, b = NMI()
        if a == b == 0:
            exit()
        if a == b == -1:
            exit()

        # print(D)

        for i, (l, r) in enumerate(D):
            if l <= a < r:
                D.pop(i)
                if a > l:
                    D.append((l, a))
                if r > a+L:
                    D.append((a+L, r))
                g_now = g_now ^ G[r-l] ^ G[a-l] ^ G[r-a-L]
                break

        # print(D)
        ok = False
        for i, (l, r) in enumerate(D):
            if r - l < L:
                continue
            g_else = g_now ^ G[r - l]
            for x in range(l, r - L+1):
                # print(l, x, x+L, r)
                if g_else ^ G[x - l] ^ G[r - (x + L)] == 0:
                    print(x, L)
                    sys.stdout.flush()
                    g_now = g_else ^ G[x - l] ^ G[r - (x + L)]
                    D.pop(i)
                    if x - l > 0:
                        D.append((l, x))
                    if r - (x + L) > 0:
                        D.append((x + L, r))
                    ok = True
                    break
            if ok:
                break

        if not ok:
            print("error")


def copycat_tactics(N, L, R):
    print("First")
    sys.stdout.flush()

    for y in range(L, R+1):
        if N % 2 == y % 2:
            g = (N - y) // 2
            print(g+1, y)
            sys.stdout.flush()
            break

    def rev(a):
        return N+1 - a

    while True:
        a, b = NMI()
        if a == b == -1 or a == b == 0:
            exit()

        x = rev(a+b-1)
        y = b
        print(x, y)
        sys.stdout.flush()


def main():
    N, L, R = NMI()
    if L == R and N % 2 != L % 2:
        grundy_tactics(N, L, R)
    else:
        copycat_tactics(N, L, R)


if __name__ == "__main__":
    main()
