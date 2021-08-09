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


def main():
    N, sh, sw = NMI()
    grid = [SI() for _ in range(N)]

    graph = defaultdict(list)

    LURD = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    Cross = set()

    for h in range(N):
        for w in range(N):
            h_cnt = 0
            w_cnt = 0
            for dh, dw in LURD:
                nh, nw = h+dh, w+dw
                if nh < 0 or nh >= N or nw < 0 or nw >= N:
                    continue
                if grid[nh][nw] != "#":
                    if dh == 0:
                        w_cnt += 1
                    else:
                        h_cnt += 1
            if w_cnt > 0 and h_cnt > 0:
                Cross.add((h, w))

    print(Cross)
    print(len(Cross))


    for ph, pw in Cross:
        #縦走査
        for dh in range(1, N):
            nh = ph + dh
            nw = pw
            if nh >= N or nw >= N:
                break
            if grid[nh][nw] == "#":
                break
            if (nh, nw) in Cross:
                print((ph, pw), (nh, nw))
                graph[(ph, pw)].append((nh, nw))
                graph[(nh, nw)].append((ph, pw))

        # 横走査
        for dw in range(1, N):
            nh = ph
            nw = pw + dw
            if nh >= N or nw >= N:
                break
            if grid[nh][nw] == "#":
                break
            if (nh, nw) in Cross:
                print((ph, pw), (nh, nw))
                graph[(ph, pw)].append((nh, nw))
                graph[(nh, nw)].append((ph, pw))

    #print(*graph.items(), sep="\n")

    def is_ng_hw(h, w):
        if h < 0 or h >= N or w < 0 or w >= N:
            return True
        if grid[h][w] == "#":
            return True
        return False


    # 最初の移動
    first_node = None
    for dh, dw in LURD:
        for i in range(N):
            nh, nw = sh + dh*i, sw + dw*i
            if is_ng_hw(nh, nw):
                break
            if (nh, nw) in Cross:
                first_node = (nh, nw)
                break

        if first_node:
            break

    print(first_node)



if __name__ == "__main__":
    main()
