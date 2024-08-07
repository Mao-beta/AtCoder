import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W = NMI()
    G = [SI() for _ in range(H)]

    queue = deque()

    seen = [[[0] * W for _ in range(H)] for _ in range(4)]
    for d in range(4):
        seen[d][1][1] = 1
    queue.append([1, 1])

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w = queue.popleft()

        print(now_h, now_w)
        print(queue)

        for d, (dh, dw) in enumerate(zip(DH, DW)):
            tmp_h = now_h
            tmp_w = now_w
            while True:
                tmp_h += dh
                tmp_w += dw
                print(now_h, now_w, d, tmp_h, tmp_w)
                if seen[d][tmp_h][tmp_w]:
                    break
                if G[tmp_h][tmp_w] == "#":
                    # if now_h != tmp_h-dh and now_w != tmp_w-dw:
                    print("#")
                    if seen[d][tmp_h-dh][tmp_w-dw]:
                        break
                    queue.append((tmp_h-dh, tmp_w-dw))
                    seen[d][tmp_h-dh][tmp_w-dw] = 1
                    break
                else:
                    seen[d][tmp_h][tmp_w] = 1
                    continue

    for row in seen:
        print()
        print(*row, sep="\n")

    ans = 0
    for h in range(H):
        for w in range(W):
            tmp = 0
            for d in range(4):
                tmp |= seen[d][h][w]
            ans += tmp
    print(ans)


if __name__ == "__main__":
    main()
