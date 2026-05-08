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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        ans = []
        ODD = set()
        EVEN = set()
        odd = True
        for i in range(2*N):
            a = A[i]
            if odd:
                if a in ODD:
                    ans.append(i)
                    EVEN.add(a)
                    odd = not odd
                else:
                    ODD.add(a)
            else:
                if a in EVEN:
                    ans.append(i)
                    ODD.add(a)
                    odd = not odd
                else:
                    EVEN.add(a)
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    main()
