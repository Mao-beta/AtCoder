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


def main():
    S = [SI() for _ in range(9)]

    def is_square(p1, p2, p3, p4):
        L = []
        for X in combinations([p1, p2, p3, p4], 2):
            l = (X[0][0] - X[1][0]) ** 2 + (X[0][1] - X[1][1]) ** 2
            L.append(l)

        L.sort()
        if L[0] * 2 == L[1] * 2 == L[2] * 2 == L[3] * 2 == L[4] == L[5]:
            return True
        else:
            return False


    ans = 0

    for p1 in range(81):
        for p2 in range(p1+1, 81):
            for p3 in range(p2+1, 81):
                for p4 in range(p3+1, 81):
                    q1 = divmod(p1, 9)
                    q2 = divmod(p2, 9)
                    q3 = divmod(p3, 9)
                    q4 = divmod(p4, 9)
                    if is_square(q1, q2, q3, q4):
                        if S[q1[0]][q1[1]] == S[q2[0]][q2[1]] == S[q3[0]][q3[1]] == S[q4[0]][q4[1]] == "#":
                            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
