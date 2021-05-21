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
    m, M = min(A), max(A)

    ans = []

    if m < 0 < M:
        if abs(M) >= abs(m):
            M_i = A.index(M)
            for i in range(N):
                ans.append([M_i+1, i+1])
                A[i] += M
        else:
            m_i = A.index(m)
            for i in range(N):
                ans.append([m_i+1, i+1])
                A[i] += m

    m, M = min(A), max(A)

    if m >= 0:
        for i in range(N-1):
            ans.append([i+1, i+2])
            A[i+1] += A[i]
    else:
        for i in range(N-1, 0, -1):
            ans.append([i+1, i])
            A[i-1] += A[i]

    print(len(ans))
    for x, y in ans:
        print(x, y)


if __name__ == "__main__":
    main()
