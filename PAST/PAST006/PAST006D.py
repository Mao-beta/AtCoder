import sys
import math
from collections import defaultdict
from collections import deque

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
    base = sum(A[0:K])
    print(base)
    for i in range(N-K):
        base = base - A[i] + A[i+K]
        print(base)


if __name__ == "__main__":
    main()
