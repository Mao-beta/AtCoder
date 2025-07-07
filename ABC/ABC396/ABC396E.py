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
    N, M = NMI()
    XYZ = EI(M)
    XYZ = [[x-1, y-1, w] for x, y, w in XYZ]
    ans = [0] * N
    for d in range(32):
        G = [[] for _ in range(N)]
        for x, y, z in XYZ:
            w = (z >> d) & 1
            G[x].append(y*2+w)
            G[y].append(x*2+w)

        W = [-1] * N
        for s in range(N):
            if W[s] != -1:
                continue
            D = [s]
            W[s] = 0
            Alls = []
            Ones = []
            while D:
                x = D.pop()
                Alls.append(x)
                if W[x] == 1:
                    Ones.append(x)
                for yw in G[x]:
                    y, w = divmod(yw, 2)
                    if W[y] != -1 and W[x] ^ w != W[y]:
                        print(-1)
                        exit()
                    if W[y] != -1:
                        continue
                    W[y] = W[x] ^ w
                    D.append(y)
            n = len(Alls)
            zero = n - len(Ones)
            one = len(Ones)
            if one <= zero:
                for x in Ones:
                    ans[x] |= 1 << d
            else:
                for x in set(Alls) - set(Ones):
                    ans[x] |= 1 << d
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
