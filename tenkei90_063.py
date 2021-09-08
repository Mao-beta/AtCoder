import sys
import math
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    G = [NLI() for _ in range(H)]

    ans = 0
    for case in range(1<<H):
        SG = []
        for h in range(H):
            if (case>>h) & 1:
                SG.append(G[h])
        HH = len(SG)

        C = defaultdict(int)
        tmp = 0
        is_ok = True
        for w in range(W):
            col = set()
            for i in range(HH):
                col.add(SG[i][w])
            if len(col) != 1:
                continue
            v = col.pop()
            C[v] += 1

        for _, k in C.items():
            ans = max(ans, HH*k)

    print(ans)



if __name__ == "__main__":
    main()
