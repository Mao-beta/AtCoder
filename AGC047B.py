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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    S = [SI()[::-1] for _ in range(N)]
    S.sort(key=len)
    D = []
    ans = 0
    for s in S:
        s_dict = defaultdict(list)
        for i, t in enumerate(s):
            s_dict[t].append(i)
        D.append(s_dict)

    for i, s in enumerate(S):
        for j in range(i+1, N):
            T = D[j]
            for k, ss in enumerate(s):
                if k != len(s)-1:
                    if k not in T[ss]:
                        break
                else:
                    if T[ss]:
                        if T[ss][-1] >= k:
                            ans += 1
    print(ans)


if __name__ == "__main__":
    main()