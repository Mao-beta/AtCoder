import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def main():
    N = NI()
    A = NLI()
    B = NLI()
    S = [SI() for _ in range(N)]
    A = [x-1 for x in A]
    B = [x-1 for x in B]

    if sum(A) % 2 != sum(B) % 2:
        print(-1)
        exit()

    def within(h, w):
        return 0 <= h < N and 0 <= w < N

    que = deque()
    que.append((0, *A))
    INF = 10**10

    steps = [[INF]*N for _ in range(N)]

    DH = [-1, -1, 1, 1]
    DW = [-1, 1, -1, 1]
    steps[A[0]][A[1]] = 0

    while que:
        step, h, w = que.popleft()
        if h == B[0] and w == B[1]:
            print(step)
            exit()

        if steps[h][w] < step:
            continue

        for dh, dw in zip(DH, DW):
            for k in range(1, N+1):
                nh, nw = h + dh * k, w + dw * k
                if not within(nh, nw):
                    break
                if S[nh][nw] == "#":
                    break

                if steps[nh][nw] <= step:
                    break
                if steps[nh][nw] == step + 1:
                    continue

                que.append((step+1, nh, nw))
                steps[nh][nw] = step + 1

    # print(*steps, sep="\n")
    if steps[B[0]][B[1]] == INF:
        print(-1)
        exit()

    print(steps[B[0]][B[1]])


if __name__ == "__main__":
    main()
