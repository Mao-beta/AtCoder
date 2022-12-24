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
    S = SI()
    D = deque()
    A = [0] * 26
    for s in S:
        # print(A)
        if s == "(":
            D.append(s)
        elif s == ")":
            while True:
                d = D.pop()
                if d == "(":
                    break
                else:
                    di = ord(d) - ord("a")
                    A[di] = 0

        else:
            si = ord(s) - ord("a")
            if A[si]:
                print("No")
                exit()
            else:
                D.append(s)
                A[si] = 1

    print("Yes")


if __name__ == "__main__":
    main()
