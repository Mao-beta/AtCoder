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
    S, K = SI().split()
    print("".join(sorted(list(set(permutations(S, len(S)))))[int(K)-1]))


if __name__ == "__main__":
    main()
