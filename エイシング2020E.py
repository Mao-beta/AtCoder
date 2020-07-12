import sys
import math
from collections import deque
import heapq as hq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        base = 0
        camels = [NLI() for _ in range(N)]
        camels_L = [[] for _ in range(N+1)]  # 左からi番目以内に入るとうれしい
        camels_R = [[] for _ in range(N+1)]  # 右からi番目以内に入るとうれしい
        # 左から詰めるラクダと右から詰めるラクダを仕分ける
        for camel in camels:
            if camel[1] >= camel[2]:
                camels_L[camel[0]].append(camel[1] - camel[2])
                base += camel[2]  # LとRの低いほうを加算
            else:
                camels_R[N - camel[0]].append(camel[2] - camel[1])
                base += camel[1]  # LとRの低いほうを加算
        diff = 0

        # 左から詰める
        heap_camels = []
        hq.heapify(heap_camels)
        for i in range(1, N+1):
            # 左からi番目までが限度のラクダをまとめて追加
            for camel in camels_L[i]:
                hq.heappush(heap_camels, camel)
            # 左からi番目までに入りきらない場合に低いものから除外
            while len(heap_camels) > i:
                hq.heappop(heap_camels)
        # heapqに残ったものがすべての条件を満たしうれしさが最大
        diff += sum(heap_camels)

        # 右から詰める
        heap_camels = []
        hq.heapify(heap_camels)
        for i in range(1, N+1):
            for camel in camels_R[i]:
                hq.heappush(heap_camels, camel)
            while len(heap_camels) > i:
                hq.heappop(heap_camels)
        diff += sum(heap_camels)

        print(base + diff)



if __name__ == "__main__":
    main()