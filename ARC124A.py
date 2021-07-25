import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    querys = [SI().split() for _ in range(K)]
    querys = [[int(k), c] for c, k in querys]
    querys.sort()
    case = [0] * N
    for k, c in querys:
        if c == "R":
            for i in range(k):
                case[i] += 1
        else:
            for i in range(N-1, k-1, -1):
                case[i] += 1

    for k, c in querys:
        case[k-1] = 1

    ans = 1
    for x in case:
        ans *= x
        ans %= MOD
    print(ans)



if __name__ == "__main__":
    main()
