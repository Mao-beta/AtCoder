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
    S = SI()
    N = len(S)

    if N == 2:
        if S == "10":
            print(1, 2)
            exit()
        else:
            print(-1)
            exit()

    if S[0] == "0" or S[-1] == "1" or S[-2] == "0":
        print(-1)
        exit()

    ans = []
    v = 2
    root = 1

    for k in range(N//2, 0, -1):
        rem = N - k
        if S[rem-1] != S[k-1]:
            print(-1)
            exit()

        if S[k-1] == "1" and len(ans) == 0:
            ans.append([1, 2])
            v = 3
            continue

        if S[k-1] == "0" and len(ans) == 0:
            continue

        if S[k-1] == "0":
            ans.append([root, v])
            v += 1
        else:
            ans.append([root, v])
            root = v
            v += 1

    for i in range(N-1 - len(ans)):
        ans.append([2, v])
        v += 1

    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
