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
    LR = [NLI() for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            tmp = 0
            li, ri = LR[i]
            lj, rj = LR[j]
            for xi in range(li, ri+1):
                for xj in range(lj, rj+1):
                    if xi > xj:
                        tmp += 1
            ans += tmp / ((ri-li+1)*(rj-lj+1))

    print(ans)


if __name__ == "__main__":
    main()
