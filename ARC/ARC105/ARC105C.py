import sys
import math
from collections import deque
from itertools import permutations
from itertools import combinations
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M = NMI()
    W = NLI()
    B = [NLI()[::-1] for _ in range(M)]
    cases = list(permutations(W, N))
    all_weights = set(W)
    for r in range(2, N+1):
        for comb in combinations(W, r):
            all_weights.add(sum(comb))
    all_weights = sorted(list(all_weights))

    B.sort()
    now_l = 0
    for i, [v, l] in enumerate(B):
        now_l = max(now_l, l)
        B[i][1] = now_l

    if max(W) > B[0][0]:
        print(-1)
        exit()

    V = [b[0] for b in B]
    L = [b[1] for b in B]
    weight_to_idx = {}
    for w in all_weights:
        weight_to_idx[w] = bisect.bisect_right(V, w)

    ans = 10 ** 20
    for camels in cases:
        X = [0] * N
        for i in range(N):
            for j in range(i+2, N+1):
                w = sum(camels[i:j])
                idx = weight_to_idx[w]
                if idx == 0:
                    X[j-1] = max(X[i], X[j-1])
                else:
                    X[j-1] = max(X[i]+L[idx-1], X[j-1])
        ans = min(ans, X[-1])
    print(ans)



if __name__ == "__main__":
    main()
