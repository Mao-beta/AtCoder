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
    N = NI()
    A = NLI()
    B = NLI()
    AS = sorted(A)
    BS = sorted(B)
    for a, b in zip(AS, BS):
        if a > b:
            print("No")
            exit()

    for i, a in enumerate(A):
        
    print("Yes")


if __name__ == "__main__":
    main()
