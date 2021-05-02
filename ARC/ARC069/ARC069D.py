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
    S = SI()
    SS = [1, 1]
    SW = [1, -1]
    WS = [-1, 1]
    WW = [-1, -1]
    animals = [SS, SW, WS, WW]

    for i, s in enumerate(S+S[0]):
        if i == 0: continue
        for A in animals:
            if s == "o":
                A.append(A[i-1]*A[i])
            else:
                A.append(-A[i-1]*A[i])

    for A in animals:
        if A[0] == A[-2] and A[1] == A[-1]:
            ans = ["S" if a == 1 else "W" for a in A]
            print("".join(ans[:-2]))
            exit()
    print(-1)


if __name__ == "__main__":
    main()
