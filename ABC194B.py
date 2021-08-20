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
    AB = [NLI() for _ in range(N)]
    ans = 10**10
    for i in range(N):
        for j in range(N):
            a = AB[i][0]
            b = AB[j][1]
            if i == j:
                ans = min(ans, a+b)
            else:
                ans = min(ans, max(a, b))
    print(ans)



if __name__ == "__main__":
    main()
