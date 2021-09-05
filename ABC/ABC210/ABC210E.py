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
    N, M = NMI()
    AC = [NLI() for _ in range(M)]
    AC.sort(key=lambda x: x[1])
    ans = 0
    num = 0
    ok_num = N-1

    for a, c in AC:
        g = math.gcd(N, a)
        ans += (N-g) * c
        num += N-g
        N = g

    if num != ok_num:
        print(-1)
    else:
        print(ans)



if __name__ == "__main__":
    main()
