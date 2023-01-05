import sys
import math
import bisect
import time
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
from random import randint


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


def print_err(*args):
    print(*args, file=sys.stderr)

def output_file(ans, outpath):
    with open(outpath, "w") as f:
        for d in ans:
            f.write(str(d) + "\n")

def output(ans):
    print(*ans, sep="\n")

def input_file(path):
    with open(path, mode="r") as f:
        inputs = f.readlines()
        N, K, L = map(int, inputs[0].split())
        AB = [[0, 0]]
        AB += [list(map(int, inputs[1 + i].split())) for i in range(K)]
        C = [list(map(int, inputs[1 + K + i].split())) for i in range(N)]
    return N, K, L, AB, C

def input_judge():
    N, K, L = NMI()
    AB = [[0, 0]] + EI(K)
    C = EI(N)
    return N, K, L, AB, C


def main(N, K, L, AB, C):
    START_TIME = time.time()

    # 地区の隣接リスト
    G: list = [set() for _ in range(K+1)]

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    for h in range(N):
        for w in range(N):
            c = C[h][w]
            if c == 0:
                continue

            for dh, dw in zip(DH, DW):
                nh = h + dh
                nw = w + dw
                if not(0 <= nh < N and 0 <= nw < N):
                    continue

                nc = C[nh][nw]
                if nc == 0:
                    continue
                if c == nc:
                    continue

                G[c].add(nc)
                G[nc].add(c)

    # print_err("G", G)

    def calc_score(_D):
        # 同じ特別区内をDFS
        # どの特別区を見たか覚えておく
        # 連結でなければ0点
        # 全特別区がなければ0点
        seen_D = set()
        P = [0] * (L+1)
        Q = [0] * (L+1)

        seen = [0] * (K+1)

        for s in range(1, K+1):
            d = _D[s]
            if seen[s]:
                continue

            if d in seen_D:
                return 0.0

            seen_D.add(d)

            stack = deque()
            stack.append(s)
            seen[s] = 1
            while stack:
                now = stack.pop()
                P[d] += AB[now][0]
                Q[d] += AB[now][1]
                for goto in G[now]:
                    if seen[goto]:
                        continue
                    if _D[goto] != d:
                        continue
                    stack.append(goto)
                    seen[goto] = 1

        P = P[1:]
        Q = Q[1:]
        pmax = max(P)
        pmin = min(P)
        qmax = max(Q)
        qmin = min(Q)
        if pmin == 0 or qmin == 0:
            return 0.0

        # print_err("P", P)
        # print_err("Q", Q)
        # print_err(seen)

        return round(10**6 * min(pmin/pmax, qmin/qmax))

    best_D = [0] * (K+1)
    best_score = 0

    for _ in range(100):
        # 特別区の番号
        tmp_D: list = [0] * (K+1)

        # 始点をL個決める
        for d in range(1, L+1):
            while True:
                s = randint(1, K)
                if tmp_D[s] == 0:
                    tmp_D[s] = d
                    break

        # 多始点BFS
        que = deque()
        for s, d in enumerate(tmp_D):
            if d > 0:
                que.append([s, d])

        # print_err(len(que), que)

        while que:
            now, d = que.popleft()
            for goto in G[now]:
                if tmp_D[goto] > 0:
                    continue
                tmp_D[goto] = d
                que.append([goto, d])

        score = calc_score(tmp_D)
        print_err(score)
        if score > best_score:
            best_score = score
            best_D = tmp_D[:]

    D = best_D[:]
    print_err(round(time.time() - START_TIME, 3), best_score)

    while time.time() - START_TIME < 0.83:
        s = randint(1, K)
        new_d = D[list(G[s])[randint(0, len(G[s])-1)]]
        old_d = D[s]
        D[s] = new_d
        tmp_score = calc_score(D[:])
        if tmp_score > best_score:
            best_score = tmp_score
            best_D = D[:]
            print_err(tmp_score, best_score)
        else:
            D[s] = old_d


    print_err("FINAL_SCORE", calc_score(best_D))
    print_err("D", best_D)

    return best_D[1:]


IS_LOCAL = True
try:
    import matplotlib
except ImportError:
    IS_LOCAL = False


if __name__ == "__main__":
    if IS_LOCAL:
        for i in range(1):
            path = f"./C20_in/in{str(i).zfill(3)}.txt"
            outpath = f"./C20_out/out{str(i).zfill(3)}.txt"

            N, K, L, AB, C = input_file(path)
            ans = main(N, K, L, AB, C)
            output_file(ans, outpath)

    else:
        N, K, L, AB, C = input_judge()
        ans = main(N, K, L, AB, C)
        output(ans)
