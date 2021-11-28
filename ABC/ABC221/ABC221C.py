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
    N = SI()
    K = len(N)
    ans = 0
    for case in range(1<<K):
        S = []
        T = []
        for i in range(K):
            if (case >> i) & 1:
                S.append(N[i])
            else:
                T.append(N[i])
        S.sort(reverse=True)
        T.sort(reverse=True)
        if not S or not T:
            continue
        S = int("".join(S))
        T = int("".join(T))
        ans = max(ans, S*T)

    print(ans)


if __name__ == "__main__":
    main()
