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
    N, Q = NMI()
    XYZW = [NLI() for _ in range(Q)]

    ans = 1

    # 下からi桁目
    for i in range(60):
        tmp = 0
        for case in range(1<<N):
            ok = True
            for x, y, z, w in XYZW:
                x, y, z = x-1, y-1, z-1
                bx = (case >> x) & 1
                by = (case >> y) & 1
                bz = (case >> z) & 1
                bw = (w >> i) & 1
                if (bx | by | bz) != bw:
                    ok = False
            if ok:
                tmp += 1
        ans = ans * tmp % MOD

    print(ans)


if __name__ == "__main__":
    main()
