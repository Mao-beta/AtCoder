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
    S = SI()

    for _ in range(K):
        tmp = []
        SS = S * 2
        for i in range(0, 2*N, 2):
            a, b = SS[i], SS[i+1]
            if a == b:
                tmp.append(a)
            elif (a, b) in {("R", "S"), ("P", "R"), ("S", "P")}:
                tmp.append(a)
            else:
                tmp.append(b)
        S = "".join(tmp)

    print(S[0])


if __name__ == "__main__":
    main()
