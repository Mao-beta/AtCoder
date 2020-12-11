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
    N, H = NMI()
    A, B, C, D, E = NMI()
    ans = 10**20
    for i in range(N+1):
        no_food = i
        n = math.ceil((H + N * B - no_food * (E+B)) / (B-D))
        if n > 0:
            sisso = min(n - 1, N - no_food)
            normal = N - no_food - sisso
            ans = min(ans, sisso*C + normal*A)
        else:
            break

    print(ans)


if __name__ == "__main__":
    main()
