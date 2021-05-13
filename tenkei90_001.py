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
    N, L = NMI()
    K = NI()
    A = [0] + NLI() + [L]
    A = [A[i+1] - A[i] for i in range(N+1)]

    def is_ok(x):
        rem = 0
        cut = 0
        for a in A:
            rem += a
            if rem >= x and cut < K:
                rem = 0
                cut += 1
        if rem >= x and cut == K:
            return True
        else:
            return False

    ok = 0
    ng = 10**10
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
