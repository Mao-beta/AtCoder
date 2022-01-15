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


alp_to_num = {chr(i+97): i for i in range(26)}


def main():
    S = list(SI())
    S = list(map(lambda x: alp_to_num[x], S))
    # print(S)
    ans = 200
    for target in range(26):
        SS = S[:]
        num = 0
        while len(set(SS)) > 1:
            # print(SS)
            T = []
            for i in range(len(SS) - 1):
                a, b = SS[i], SS[i+1]
                if a == target or b == target:
                    T.append(target)
                else:
                    T.append(a)
            SS = T[:]
            num += 1
        ans = min(ans, num)
    print(ans)


if __name__ == "__main__":
    main()
