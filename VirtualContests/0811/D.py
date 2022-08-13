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
    A = NLI()

    if len(set(A)) == 1:
        print(N//2)
        exit()

    CA = Counter(A[::2])
    CB = Counter(A[1::2])

    CA[-1] = 0
    CB[-1] = 0

    CA = CA.most_common()
    CB = CB.most_common()


    if CA[0][0] != CB[0][0]:
        print(N - CA[0][1] - CB[0][1])
        exit()

    ans = N
    for ai in range(2):
        for bi in range(2):
            if CA[ai][0] == CB[bi][0]: continue
            ans = min(ans, N - CA[ai][1] - CB[bi][1])

    print(ans)




if __name__ == "__main__":
    main()
