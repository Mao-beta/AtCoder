import sys
import math
from collections import deque
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
    H = sorted(NLI())
    W = sorted(NLI())

    if N == 1:
        gap = [abs(H[0]-w) for w in W]
        print(min(gap))
        exit()

    W_idx = [bisect.bisect_left(H, w) for w in W]
    gaps = []
    for i in range(N-1):
        gaps.append(H[i+1] - H[i])

    cum_front = [0]
    for g in gaps[::2]:
        cum_front.append(cum_front[-1] + g)
    cum_back = [0]
    for g in gaps[::-1][::2]:
        cum_back.append(cum_back[-1] + g)

    ans = 10**20
    for wi, w in enumerate(W):
        w_idx = W_idx[wi]
        if w_idx % 2:
            tmp = cum_front[(w_idx-1)//2] + cum_back[(N-w_idx)//2] + w - H[w_idx-1]
        else:
            tmp = cum_front[w_idx // 2] + cum_back[(N - w_idx - 1) // 2] + H[w_idx] - w
        ans = min(ans, tmp)
    print(ans)





if __name__ == "__main__":
    main()
