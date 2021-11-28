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
    ans = 0
    for i in range(1, N-1):
        a, b, c = A[i-1], A[i], A[i+1]
        if (b-a)*(c-b) > 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
