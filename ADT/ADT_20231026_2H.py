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
    N, X, Y = NMI()
    A = NLI()

    # MX[i]: i以降でXを超える左端
    # MY[i]: i以降でYを下回る左端
    MX = [N] * (N+1)
    MY = [N] * (N+1)
    mx, my = N, N
    for i in range(N-1, -1, -1):
        if A[i] > X:
            mx = i
        if A[i] < Y:
            my = i
        MX[i] = mx
        MY[i] = my

    D = deque()
    C = Counter()
    r = 0
    ans = 0
    for l in range(N):
        if r < l:
            r = l

        while r < N and (C[X] == 0 or C[Y] == 0) and Y <= A[r] <= X:
            D.append(A[r])
            C[A[r]] += 1
            r += 1

        if C[X] > 0 and C[Y] > 0:
            rem = min(MX[r], MY[r]) - r
            ans += rem + 1

        if D:
            a = D.popleft()
            C[a] -= 1

    print(ans)


if __name__ == "__main__":
    main()
