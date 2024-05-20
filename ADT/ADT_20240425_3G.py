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
    N, D = NMI()
    LR = EI(N)
    LR = [[x, y+1] for x, y in LR]
    LR.sort(key=lambda x: x[1])
    LR = deque(LR)
    ans = 0
    nowr = -1
    while LR:
        nowr = LR[0][1] + D-1
        while LR:
            if LR[0][0] < nowr:
                LR.popleft()
            else:
                break
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
