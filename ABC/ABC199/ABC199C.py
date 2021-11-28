import sys
import math
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
    S = list(SI())
    Q = NI()
    top = 0
    for _ in range(Q):
        t, a, b = NMI()
        a, b = a-1, b-1
        if t == 1:
            a = (a + top) % (2*N)
            b = (b + top) % (2*N)
            S[a], S[b] = S[b], S[a]
        else:
            top = (top + N) % (2*N)

    ans = "".join(S)
    if top == N:
        ans = ans[N:] + ans[:N]
    print(ans)


if __name__ == "__main__":
    main()
