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
    A = [a&(-a) for a in A]
    one = A.count(1)
    two = A.count(2)
    four = N - one - two
    if one >= four + 2:
        print("No")
    elif one == four + 1:
        if one + four == N:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
