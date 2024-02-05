import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    x, y = NMI()
    N = NI()
    XY = EI(N) * 2
    ans = 10**9
    for i in range(N):
        A, B = XY[i], XY[i+1]
        px, py = B[0]-A[0], B[1]-A[1]
        qx, qy = x-A[0], y-A[1]
        rx, ry = x-B[0], y-B[1]
        q2 = qx**2 + qy**2
        pq = px * qx + py * qy
        p2 = px**2 + py**2
        r2 = rx**2 + ry**2
        d2 = q2 - pq**2 / p2
        if pq > p2 or pq < 0:
            ans = min(ans, min(math.sqrt(q2), math.sqrt(r2)))
        else:
            ans = min(ans, min(math.sqrt(q2), math.sqrt(r2), math.sqrt(d2)))
    print(ans)


if __name__ == "__main__":
    main()
