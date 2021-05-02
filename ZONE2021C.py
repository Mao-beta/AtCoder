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
    skills = [NLI() for _ in range(N)]

    ok = 0
    ng = 2 * 10 ** 9
    while abs(ok - ng) > 1:

        mid = (ok + ng) // 2

        U = [0] * (1 << 5)
        for skill in skills:
            u = 0
            for i, s in enumerate(skill):
                if s >= mid:
                    u += 1 << i
            U[u] += 1

        is_ok = False

        if U[-1] >= 1:
            is_ok = True
        else:
            for i in range(30):
                for j in range(i + 1, 31):
                    for k in range(j + 1, 32):
                        if U[i] == 0 or U[j] == 0 or U[k] == 0:
                            continue

                        if i | j | k == 31:
                            is_ok = True

        if is_ok:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
