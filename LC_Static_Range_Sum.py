import sys
import math
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, Q = NMI()
    A = [0] + NLI()
    C = list(accumulate(A))
    for _ in range(Q):
        l, r = NMI()
        print(C[r] - C[l])


if __name__ == "__main__":
    main()
