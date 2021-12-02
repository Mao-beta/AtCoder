import random
import sys
import time
from collections import deque
from pathlib import Path
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False

#IS_LOCAL = False


def move_robot(grid, order, robot, L_robots, R_robots):
    URDL = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    d = 0
    nh, nw = 14, 14
    path = [[nh, nw]]
    for s in order:
        if s == "S":
            dh, dw = URDL[d]
            nh += dh
            nw += dw
            if grid[nh][nw] == "#":
                nh -= dh
                nw -= dw
        elif s == "R":
            R_robots[(nh, nw)].add(robot)
            d = (d+1) % 4
            if grid[nh][nw] == "L":
                d = (d-2) % 4
        elif s == "L":
            L_robots[(nh, nw)].add(robot)
            d = (d-1) % 4
            if grid[nh][nw] == "R":
                d = (d-2) % 4
        path.append([nh, nw])

    return nh, nw, path


def solve(values):
    start_time = time.time()
    TIME_LIMIT = 2.5
    N, M, L, S = values
    S = [list(s) for s in S]

    # 初期配置
    ans = [["."]*M for _ in range(M)]
    for h in range(M):
        ans[h][0] = "#"
        ans[h][-1] = "#"
    for w in range(M):
        ans[0][w] = "#"
        ans[-1][w] = "#"

    # 初期移動
    # hw -> idx
    # あるhwでL/Rを実行したrobotのidxのset
    L_robots = defaultdict(set)
    R_robots = defaultdict(set)

    robots_dst = []
    dests = [[0]*M for _ in range(M)]
    for i, s in enumerate(S):
        h, w, path = move_robot(ans, s, i, L_robots, R_robots)
        dests[h][w] += 1
        robots_dst.append([h, w])

    # 初期得点計算
    score_dict = defaultdict(int)
    score_dict[1] = 10
    score_dict[2] = 3
    score_dict[3] = 1

    score = 0
    for h in range(M):
        for w in range(M):
            score += score_dict[dests[h][w]]

    if IS_LOCAL:
        print(score)

    # 山登り
    loop_cnt = 1
    paths = [[] for _ in range(N)]

    while True:
        rh = random.randint(1, M-2)
        rw = random.randint(1, M-2)
        rs = ".LR"[random.randint(0, 2)]
        while rs == ans[rh][rw]:
            rs = ".LR"[random.randint(0, 2)]

        bs = ans[rh][rw]
        ans[rh][rw] = rs

        targets = list(R_robots[(rh, rw)] & L_robots[(rh, rw)])
        HWs = []
        BHWs = []
        for robot in targets:
            h, w, path = move_robot(ans, S[robot], robot, L_robots, R_robots)
            paths[robot] = path
            bh, bw = robots_dst[robot]
            robots_dst[robot][0] = h
            robots_dst[robot][1] = w
            dests[bh][bw] -= 1
            dests[h][w] += 1
            HWs.append((h, w))
            BHWs.append((bh, bw))

        tmp_score = 0
        for h in range(M):
            for w in range(M):
                tmp_score += score_dict[dests[h][w]]

        if tmp_score > score:
            score = tmp_score

        else:
            ans[rh][rw] = bs
            for (h, w), (bh, bw), robot in zip(HWs, BHWs, targets):
                th, tw, path = move_robot(ans, S[robot], robot, L_robots, R_robots)
                paths[robot] = path
                robots_dst[robot][0] = th
                robots_dst[robot][1] = tw
                dests[th][tw] += 1
                dests[h][w] -= 1

        loop_cnt += 1

        if time.time() - start_time > TIME_LIMIT:
            break

    if IS_LOCAL:
        print(loop_cnt, score)
        print(*dests, sep="\n")
        print(sum([sum(r) for r in dests]))

        for robot in range(389, 391):
            print(paths[robot])

    return ans



def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write("".join(map(str, row)) + "\n")
    else:
        for row in ans:
            print(*row, sep="")


def input_values(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, M, L = map(int, inputs[0].split())
            S = inputs[1:]

    else:
        N, M, L = NMI()
        S = [SI() for _ in range(N)]

    return N, M, L, S


def main(file=None):
    in_path = None
    out_path = None

    if file:
        in_filename = file + ".in"
        in_path = Path("./in/") / in_filename
        out_filename = file + ".out"
        out_path = Path("./out/") / out_filename

    values = input_values(in_path)
    ans = solve(values)
    output_ans(ans, out_path)


if __name__ == "__main__":
    if IS_LOCAL:
        for i in range(1):
            random.seed(i)
            main(str(i).zfill(3))
    else:
        main()
