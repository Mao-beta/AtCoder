import sys
import bisect
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    A = NLI()
    A.sort()
    C = list(accumulate([0]+A))

    if (K + sum(A))//N >= max(A):
        print((K+sum(A))//N)
        exit()

    M = A[-1]
    for g in range(M, 0, -1):
        k = 0
        prev = 0
        for b in range(g, M+g, g):
            idx = bisect.bisect_right(A, b)
            k += b * (idx - prev) - (C[idx] - C[prev])
            prev = idx
        if k <= K:
            print(g)
            exit()


if __name__ == "__main__":
    main()
