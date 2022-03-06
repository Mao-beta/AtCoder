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
    ans = 0
    cum = 0
    for k in range(1, 10**6+1):
        # x: []がk以上となる個数
        x = N // k
        y = N // (k+1)
        n = x - y
        ans += k * n
        cum += n

    if cum == N:
        print(ans)
        exit()

    for i in range(1, 10**6+1):
        ans += N // i
        cum += 1
        if cum == N:
            break

    print(ans)


if __name__ == "__main__":
    main()
