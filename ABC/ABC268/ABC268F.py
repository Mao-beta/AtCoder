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
    N = NI()
    S = [SI() for _ in range(N)]

    T = []
    for i, s in enumerate(S):
        x = 0
        n = 0
        for ss in s:
            if ss == "X":
                x += 1
            else:
                n += int(ss)

        T.append([x, n, S[i]])

    T.sort(key=lambda x: x[1] / x[0] if x[0] > 0 else 10**15)

    A = []
    for i in range(N):
        A.append(T[i][2])

    A = "".join(A)

    num = 0
    ans = 0
    for a in A:
        if a == "X":
            num += 1
        else:
            ans += num * int(a)
    print(ans)


if __name__ == "__main__":
    main()
