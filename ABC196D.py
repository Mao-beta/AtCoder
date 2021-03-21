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
    H, W, A, B = NMI()
    naive_points = set()
    for h in range(H):
        for w in range(W):
            naive_points.add((h, w))
    rect_points = set()

    def rec(now_naive, now_rect):
        if len(now_rect) == 2*A:
            return 1
        elif len(now_naive) == 0:
            return 0

        now_h, now_w = now_naive.pop()
        #print(now_h, now_w)
        #print(now_naive, now_rect)
        gotos = [(now_h-1, now_w),
                 (now_h+1, now_w),
                 (now_h, now_w-1),
                 (now_h, now_w+1)]
        res = 0
        for goto in gotos:
            if goto in now_naive:
                goto_naive = now_naive.copy()
                goto_naive.discard(goto)
                goto_rect = now_rect.copy()
                goto_rect.add((now_h, now_w))
                goto_rect.add(goto)
                #print(goto_naive, goto_rect)
                res += rec(goto_naive, goto_rect)
        res += rec(now_naive, now_rect)
        #print("return", res)
        return res

    print(rec(naive_points, rect_points))


if __name__ == "__main__":
    main()
