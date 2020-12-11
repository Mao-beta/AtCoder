import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, MA, MB = NMI()
    D = []
    for _ in range(N):
        a, b, c = NMI()
        t = a*MB - b*MA
        D.append((t, c))
    D.sort()

    D1 = D[:N//2]
    D2 = D[N//2:]
    ld1 = len(D1)
    ld2 = len(D2)

    S1 = defaultdict(lambda: 10**5)
    for case in range(2**ld1):
        if case == 0: continue
        s, c = 0, 0
        for i in range(ld1):
            if (case>>i)&1:
                s += D1[i][0]
                c += D1[i][1]
        S1[s] = min(S1[s], c)

    S2 = defaultdict(lambda: 10**5)
    for case in range(2 ** ld2):
        if case == 0: continue
        s, c = 0, 0
        for i in range(ld2):
            if (case >> i) & 1:
                s += D2[i][0]
                c += D2[i][1]
        S2[s] = min(S2[s], c)

    ans = 10**5
    for s, c in list(S1.items()):
        ans = min(ans, c + S2[-s])
    ans = min(ans, S1[0], S2[0])
    if ans >= 10**5:
        print(-1)
    else:
        print(ans)



if __name__ == "__main__":
    main()