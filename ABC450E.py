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
    X = SI()
    Y = SI()
    x = len(X)
    y = len(Y)
    Q = NI()
    F = [x, y]
    while F[-1] < 10**18:
        F.append(F[-1] + F[-2])

    CX = Counter(X)
    CY = Counter(Y)

    C2K = [[CX[chr(ord("a")+i)], CY[chr(ord("a")+i)]] for i in range(26)]
    for i in range(26):
        for _ in range(len(F)-2):
            C2K[i].append(C2K[i][-1] + C2K[i][-2])

    def calc(b, c):
        # [0, b)における文字cの個数
        res = 0
        while b > 0:
            if b <= y:
                res += Y[:b].count(chr(c + ord("a")))
                break
            if b <= x+y:
                res += X[:b-y].count(chr(c + ord("a"))) + C2K[c][1]
                break
            idx = bisect.bisect_right(F, b)
            b -= F[idx-1]
            res += C2K[c][idx-1]
        return res


    for _ in range(Q):
        L, R, C = SMI()
        L = int(L)-1
        R = int(R)
        kr, kl = calc(R, ord(C)-ord("a")), calc(L, ord(C)-ord("a"))
        # print(L, R, kr, kl)
        print(kr - kl)


if __name__ == "__main__":
    main()
