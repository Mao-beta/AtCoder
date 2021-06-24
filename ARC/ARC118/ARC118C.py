import sys
import math
from collections import deque
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    P = {2, 3, 5}
    S = set()
    for a, b in permutations(P, 2):
        S.add(a*b)

    T = set()
    for i in range(1, 5000):
        for s in S:
            if s * i <= 10000:
                T.add(s*i)

    T.discard(6)
    T.discard(10)
    T.discard(15)
    T = sorted(list(T))[:N-3]
    print(6, 10, 15, *T)


if __name__ == "__main__":
    main()
