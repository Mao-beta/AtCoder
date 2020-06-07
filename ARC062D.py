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
    S = SI()
    N = len(S)
    A = "gp" * (N//2 + 1)
    ans = 0
    for i in range(N):
        if S[i] == A[i]:
            continue
        if S[i] == "g":
            ans += 1
            continue
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()