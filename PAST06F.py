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
    N, L, T, X = NMI()
    tasks = [NLI() for _ in range(N)]

    ans = 0
    load_time = 0
    for a, b in tasks:
        if b < L:
            load_time = 0
            ans += a
        else:
            if a > T:
                print("forever")
                exit()

            if load_time + a > T:
                ans += T - load_time
                ans += X
                load_time = 0

            ans += a
            load_time += a

            if load_time >= T:
                ans += X
                load_time = 0

    print(ans)


if __name__ == "__main__":
    main()
