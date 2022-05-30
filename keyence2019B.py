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
    S = list(S)
    t = len(S) - 7

    for l in range(len(S)+1 - t):
        r = l + t
        # print(S[l:r])
        if l == 0 and "".join(S[r:]) == "keyence":
            print("YES")
            exit()
        elif r == len(S) and "".join(S[:l]) == "keyence":
            print("YES")
            exit()
        else:
            T = "".join(S[:l] + S[r:])
            if T == "keyence":
                print("YES")
                exit()

    print("NO")


if __name__ == "__main__":
    main()
