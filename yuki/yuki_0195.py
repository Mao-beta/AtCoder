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
    X, Y, Z = sorted(NLI())
    F01 = [0, 1]
    F10 = [1, 0]
    for i in range(45):
        F01.append(F01[-1] + F01[-2])
        F10.append(F10[-1] + F10[-2])
    INF = 10**20

    if X == Z:
        X = 1
    elif X == Y:
        Y = Z

    if X == Y == Z == 1:
        print(1, 1)
        return

    ans = [INF, INF]
    for i in range(47):
        for j in range(47):
            fai, faj, fbi, fbj = F10[i], F10[j], F01[i], F01[j]
            # print(fai, faj, fbi, fbj)
            a = fbj*X - fbi*Y
            b = -faj*X + fai*Y
            d = fai*fbj - faj*fbi
            if a <= 0 or b <= 0:
                continue
            if a % d or b % d:
                continue
            a //= d
            b //= d
            ok = False
            F = [a, b]
            for _ in range(45):
                F.append(F[-1] + F[-2])

            if Z in F:
                ok = True
            if ok:
                if a < ans[0]:
                    ans = [a, b]
                elif a == ans[0] and b < ans[1]:
                    ans[1] = b

    if ans[0] > ans[1] and ans[0] not in [X, Y, Z]:
        ans = [ans[1], ans[0]+ans[1]]

    if ans[0] >= INF:
        print(-1)
    else:
        print(*ans)


if __name__ == "__main__":
    main()
