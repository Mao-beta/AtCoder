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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W, K = NMI()
    choco = [SI() for _ in range(H)]
    ans = 100000
    for case in range(2**(H-1)):
        groups = [[0]]
        for i in range(H-1):
            if (case >> i) & 1:
                groups[-1].append(i+1)
            else:
                groups.append([i+1])
        white = [0] * len(groups)

        is_badcase = False
        cut = len(groups) - 1
        for w in range(W):
            diff = [0] * len(groups)
            for gi, group in enumerate(groups):
                for h in group:
                    if choco[h][w] == "1":
                        white[gi] += 1
                        diff[gi] += 1

            if max(white) <= K:
                continue

            if max(diff) > K:
                is_badcase = True
                break

            cut += 1
            white = diff[:]
            continue

        if not is_badcase:
            ans = min(ans, cut)

    print(ans)



if __name__ == "__main__":
    main()