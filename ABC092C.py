import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = [0] + NLI() + [0] # [0, N+1]
    ans = 0
    for i in range(N+1):
        ans += abs(A[i+1] - A[i])

    ANS = [ans] * N
    for i in range(N):
        a, b, c = A[i], A[i+1], A[i+2]
        if (b-a)*(c-b) < 0:
            ANS[i] -= abs(b-a) + abs(c-b)
            ANS[i] += abs(c-a)

    print(*ANS, sep="\n")


if __name__ == "__main__":
    main()
