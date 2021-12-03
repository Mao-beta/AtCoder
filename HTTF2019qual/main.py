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
    # hw -> robot
    # あるhwでL/Rを実行したrobotのset
    L_robots = defaultdict(set)
    R_robots = defaultdict(set)

    # robot -> hw
    robots_L = [set() for _ in range(N)]
    robots_R = [set() for _ in range(N)]


    def move_robot(order, robot):

        for h, w in robots_L[robot]:
            L_robots[(h, w)].discard(robot)
        for h, w in robots_R[robot]:
            R_robots[(h, w)].discard(robot)

        robots_L[robot] = set()
        robots_R[robot] = set()

        URDL = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        d = 0
        nh, nw = 14, 14
        path = [[nh, nw]]
        for s in order:
            if s == "S":
                dh, dw = URDL[d]
                nh += dh
                nw += dw
                if ans[nh][nw] == "#":
                    nh -= dh
                    nw -= dw
            elif s == "R":
                R_robots[(nh, nw)].add(robot)
                robots_R[robot].add((nh, nw))
                if ans[nh][nw] == "L":
                    d = (d - 1) % 4
                else:
                    d = (d + 1) % 4
            elif s == "L":
                L_robots[(nh, nw)].add(robot)
                robots_L[robot].add((nh, nw))
                if ans[nh][nw] == "R":
                    d = (d + 1) % 4
                else:
                    d = (d - 1) % 4

            path.append([nh, nw])

        return nh, nw

    robots_dst = []
    dests = [[0]*M for _ in range(M)]
    for i, s in enumerate(S):
        h, w = move_robot(s, i)
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
        print(*dests, sep="\n")


    # 山登り
    loop_cnt = 1

    while True:
        rh = random.randint(1, M-2)
        rw = random.randint(1, M-2)
        rs = ".LR"[random.randint(0, 2)]
        while rs == ans[rh][rw]:
            rs = ".LR"[random.randint(0, 2)]

        bs = ans[rh][rw]
        ans[rh][rw] = rs

        NHWs = []
        BHWs = []
        targets = list(L_robots[(rh, rw)] & R_robots[(rh, rw)])
        for robot in targets:
            nh, nw = move_robot(S[robot], robot)
            bh, bw = robots_dst[robot]
            robots_dst[robot][0] = nh
            robots_dst[robot][1] = nw
            dests[bh][bw] -= 1
            dests[nh][nw] += 1
            NHWs.append((nh, nw))
            BHWs.append((bh, bw))

        tmp_score = 0
        for h in range(M):
            for w in range(M):
                tmp_score += score_dict[dests[h][w]]

        if tmp_score > score:
            score = tmp_score

        else:
            ans[rh][rw] = bs
            targets = list(L_robots[(rh, rw)] & R_robots[(rh, rw)])
            for robot in targets:
                nh, nw = move_robot(S[robot], robot)
                bh, bw = robots_dst[robot]
                robots_dst[robot][0] = nh
                robots_dst[robot][1] = nw
                dests[bh][bw] -= 1
                dests[nh][nw] += 1

        loop_cnt += 1
        if loop_cnt % 100 == 0:
            print(loop_cnt, score, tmp_score)
            #print(*dests, sep="\n")

        if time.time() - start_time > TIME_LIMIT:
            break

    tmp_score = 0
    for h in range(M):
        for w in range(M):
            tmp_score += score_dict[dests[h][w]]
    print(tmp_score)

    if IS_LOCAL:
        print(loop_cnt, score)
        print(*dests, sep="\n")
        print(sum([sum(r) for r in dests]))


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
