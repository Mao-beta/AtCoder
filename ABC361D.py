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
    N = NI()
    S = tuple(SI() + "..")
    T = tuple(SI() + "..")

    seen = set(S)

    D = deque()
    D.append([0, S])
    while D:
        d, X = D.popleft()
        # print(d, X)
        if X == T:
            print(d)
            return
        b = X.index(".")
        for i in range(N+1):
            if X[i] == "." or X[i+1] == ".":
                continue
            Y = list(X[:])
            Y[b], Y[i] = Y[i], Y[b]
            Y[b+1], Y[i+1] = Y[i+1], Y[b+1]
            Yt = tuple(Y)
            if Yt in seen:
                continue
            seen.add(Yt)
            D.append([d+1, Yt])

    print(-1)


if __name__ == "__main__":
    main()
