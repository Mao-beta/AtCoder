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
    N, K = NMI()
    S = SI()


    def check(X, Y):
        assert len(X) == len(Y)
        XX = deque(sorted(X))
        YY = deque(sorted(Y))
        n = len(XX)
        same = 0
        while XX and YY:
            if XX[0] == YY[0]:
                XX.popleft()
                YY.popleft()
                same += 1
            elif XX[0] < YY[0]:
                XX.popleft()
            else:
                YY.popleft()
        return n - same


    rem = list(S)
    rem.sort()
    T = []
    nowk = 0
    for i in range(N):
        kouho = rem[:]
        for r in rem:
            del kouho[kouho.index(r)]
            # print(i, T, rem, r, S[i+1:], kouho)
            k = check(S[i+1:], kouho)
            # print(nowk, k)
            if nowk + k + (r != S[i]) <= K:
                T.append(r)
                if r != S[i]:
                    nowk += 1
                break
            else:
                kouho.append(r)
                kouho.sort()

        rem = kouho[:]

    print("".join(T))


if __name__ == "__main__":
    main()
