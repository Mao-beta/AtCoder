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
    N, K = NMI()
    A = sorted(NLI(), reverse=True) + [0]
    rem = K
    an = 1
    ans = 0
    for i in range(N):
        start = A[i]
        end = A[i+1] + 1
        gap = start - end + 1
        if rem >= gap * an:
            rem -= gap * an
            ans += (start + end) * gap * an // 2
            an += 1
        else:
            g = rem // an
            r = rem % an
            end = start - g + 1
            ans += (start + end) * g * an // 2
            a = end - 1
            ans += a * r
            break

    print(ans)


if __name__ == "__main__":
    main()
