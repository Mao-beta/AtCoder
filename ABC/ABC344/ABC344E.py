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
    N = NI()
    START = -1
    END = -2
    A = [START] + NLI() + [END]
    Post = defaultdict(int)
    Prev = defaultdict(int)
    for i in range(N+2):
        if A[i] == START:
            Post[-1] = A[1]
        elif A[i] == END:
            Prev[-1] = A[-2]
        else:
            Post[A[i]] = A[i+1]
            Prev[A[i]] = A[i-1]
    Q = NI()
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            x, y = X
            post = Post[x]
            Post[x] = y
            Prev[y] = x
            Post[y] = post
            Prev[post] = y
        else:
            x = X[0]
            prev = Prev[x]
            post = Post[x]
            Post[prev] = post
            Prev[post] = prev

    a = START
    ans = []
    while True:
        a = Post[a]
        if a == END:
            break
        ans.append(a)
    print(*ans)


if __name__ == "__main__":
    main()
