import sys
import math
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
    D = dict()
    bit = min(N, 8)
    for case in range(1<<bit):
        s = 0
        S = set()
        for i in range(bit):
            if (case>>i)&1:
                s += A[i]
                S.add(i+1)
        s %= 200
        if D.get(s):
            T = D[s]
            print("Yes")
            print(len(T), *T)
            print(len(S), *S)
            exit()
        else:
            D[s] = S

    print("No")


if __name__ == "__main__":
    main()
