import sys
import math
from collections import deque
import heapq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M, Q = NMI()
    bags = [NLI() for _ in range(N)]
    bags.sort()
    #print(bags)
    boxes = NLI()
    querys = [NLI() for _ in range(Q)]

    for l, r in querys:
        ans = 0
        l, r = l-1, r-1
        can_boxes = []
        heapq.heapify(can_boxes)
        for i in range(M):
            if l <= i <= r:
                continue
            heapq.heappush(can_boxes, boxes[i])

        can_bags = []
        heapq.heapify(can_bags)
        #print(can_boxes)
        bag_idx = 0
        while can_boxes:
            now_box = heapq.heappop(can_boxes)

            while bag_idx < N:
                if bags[bag_idx][0] <= now_box:
                    w, v = bags[bag_idx]
                    heapq.heappush(can_bags, (-v, w))
                    bag_idx += 1
                else:
                    break
            #print(can_bags)
            if can_bags:
                v, _ = heapq.heappop(can_bags)
                #print(can_bags)
                v *= -1
                #print(v)
                ans += v

        print(ans)



if __name__ == "__main__":
    main()
