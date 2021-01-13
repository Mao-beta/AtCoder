import sys
import math
from collections import defaultdict
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
    P = tuple(NLI())
    Q = tuple(NLI())
    perm = permutations(range(1, N+1), N)
    for i, pe in enumerate(perm):
        if pe == P:
            a = i
        if pe == Q:
            b = i
    print(abs(a-b))


if __name__ == "__main__":
    main()
