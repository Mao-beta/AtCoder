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
    x = 0
    y = sum(A)
    ans = 10 ** 20
    for a in A[:-1]:
        x += a
        y -= a
        ans = min(ans, abs(x-y))
    print(ans)



if __name__ == "__main__":
    main()
