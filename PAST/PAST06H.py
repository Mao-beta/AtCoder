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
    N, M, K, Q = NMI()
    C = [NLI() for _ in range(N)]
    C.sort()
    now = 0
    T_cans = deque()
    ans = 10**20
    nt = 0
    for i, (p, t) in enumerate(C):
        if i < M:
            now += p
            if t:
                T_cans.append(p)
                nt += 1

            if i == M-1:
                ans = min(ans, now + Q * ((nt + K - 1) // K))

        else:
            if t == 1: continue
            if nt == 0: break
            now -= T_cans.pop()
            now += p
            nt -= 1
            ans = min(ans, now + Q * ((nt+K-1) // K))

    print(ans)


if __name__ == "__main__":
    main()
