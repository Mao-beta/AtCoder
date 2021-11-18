import sys
import math
from collections import deque
import random
import time

start_time = time.time()

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def path_dist(X, Y):
    n = len(X)
    ans = 0
    for i in range(n-1):
        x1, y1 = X[i], Y[i]
        x2, y2 = X[i+1], Y[i+1]
        ans += dist(x1, y1, x2, y2)

    return ans


def main():
    orders = [NLI() for _ in range(1000)]

    N = 1000
    M = 50

    # init
    ans_X = [400]
    ans_Y = [400]

    used = list(range(1, 51))
    for i in range(50):
        a, b, c, d = orders[i]
        ans_X.append(a)
        ans_Y.append(b)
        ans_X.append(c)
        ans_Y.append(d)

    ans_X.append(400)
    ans_Y.append(400)

    now_dist = path_dist(ans_X, ans_Y)
    # move
    random.seed(42)

    start_temp = 1
    end_temp = 0
    TIME_LIMIT = 1.5

    while True:
        # 何番目に回る注文か
        target_order = random.randint(0, M-1)

        # 0-999
        from_idx = used[target_order]
        to_idx = random.randint(0, N-1)

        while (to_idx + 1) in set(used):
            to_idx = random.randint(0, N-1)

        # idx*2 + 1, idx*2 + 2
        a = target_order * 2 + 1
        b = target_order * 2 + 1
        c = target_order * 2 + 2
        d = target_order * 2 + 2
        new_X = ans_X[:]
        new_Y = ans_Y[:]
        new_X[a], new_Y[b], new_X[c], new_Y[d] = orders[to_idx]
        pa, pb, pc, pd = ans_X[a], ans_Y[b], ans_X[c], ans_Y[d]
        na, nb, nc, nd = orders[to_idx]

        bef_x = ans_X[a-1]
        bef_y = ans_Y[a-1]
        next_x = ans_X[c+1]
        next_y = ans_Y[d+1]

        new_dist = now_dist - dist(bef_x, bef_y, pa, pb) - dist(pa, pb, pc, pd) - dist(pc, pd, next_x, next_y)
        new_dist += dist(bef_x, bef_y, na, nb) + dist(na, nb, nc, nd) + dist(nc, nd, next_x, next_y)

        #new_dist = path_dist(new_X, new_Y)

        #temp = start_temp + (end_temp - start_temp) * (time.time() - start_time) / TIME_LIMIT
        #prob = temp
        #R = random.random()

        if new_dist < now_dist:# or prob > R:
            now_dist = new_dist
            ans_X[a], ans_Y[b], ans_X[c], ans_Y[d] = orders[to_idx]
            used[target_order] = to_idx + 1

        elapsed = time.time() - start_time
        if elapsed > TIME_LIMIT:
            break

    # output
    print(M, *used)

    print(len(ans_X), end=" ")
    for x, y in zip(ans_X, ans_Y):
        print(x, y, end=" ")
    #print()

    #print(path_dist(ans_X, ans_Y))


if __name__ == "__main__":
    main()
