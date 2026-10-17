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
    S = SI()
    N = len(S) // 4
    for i in range(N):
        s = S[4*i: 4*i+4]
        if s == "post":
            print(i+1)
            exit()
    print("none")


if __name__ == "__main__":
    main()
