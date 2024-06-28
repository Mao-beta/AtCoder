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
    N, Q = NMI()
    A = NLI()
    querys = EI(Q)

    sz = 1000
    B = (N+sz-1) // sz
    C = [Counter(A[i*sz:(i+1)*sz]) for i in range(B)]
    # print(C)

    for q, *X in querys:
        if q == 0:
            k, v = X
            p = A[k]
            C[k//sz][p] -= 1
            C[k//sz][v] += 1
            A[k] = v
        else:
            l, r, x = X
            bl = (l+sz-1)//sz*sz
            br = r//sz*sz
            ans = 0
            if bl >= br:
                ans += A[l:r].count(x)
            else:
                ans += A[l:bl].count(x) + A[br:r].count(x)
                for bi in range(bl//sz, br//sz):
                    ans += C[bi][x]
            # print(l, r, bl, br, x)
            print(ans)
        # print(C)



if __name__ == "__main__":
    main()
