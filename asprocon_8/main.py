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
    S, C, H, a, b = NMI()
    N = [NLI() for _ in range(S)]
    K = NLI()
    A = [NLI() for _ in range(S)]
    B = [NLI() for _ in range(C)]

    Combare = [[-1, -1] for _ in range(H)] # 形、色
    Hangers = [[k, 0] for k in K] # 未, 使用中
    Products = [[[N[s][c], 0, 0] for c in range(C)] for s in range(S)] # 未、コンベア上、済

    def cost(si, ci, sj, cj):
        return max(A[si][sj], B[ci][cj])

    d_idx = 0 # 現在の指示位置
    h_idx = d_idx % H # 現在のコンベア位置
    Directions = [-2] * (10**6)
    finished = 0

    prev = [0, 0]

    for c in range(C):
        for s in range(S):
            # print(d_idx, h_idx)
            # 前のと違ったら待機
            if prev != [s, c]:
                d_idx += cost(prev[0], prev[1], s, c)
                # print(cost(prev[0], prev[1], s, c))
                h_idx = d_idx % H

            while Products[s][c][0] > 0:
                # 回収
                if Combare[h_idx] != [-1, -1]:
                    cs, cc = Combare[h_idx]
                    Hangers[cs][0] += 1
                    Hangers[cs][1] -= 1
                    Products[cs][cc][1] -= 1
                    Products[cs][cc][2] += 1
                    Combare[h_idx] = [-1, -1]

                # 吊るす
                if Hangers[s][0] > 0 and Products[s][c][0] > 0:
                    Hangers[s][0] -= 1
                    Hangers[s][1] += 1
                    Combare[h_idx] = [s, c]
                    Products[s][c][0] -= 1
                    Products[s][c][1] += 1
                    Directions[d_idx] = [s+1, c+1]

                # 進める
                d_idx += 1
                h_idx = d_idx % H
                assert Hangers[s][0] >= 0
                # print(Combare)
                # print(s, c, Products[s][c][0])

            prev = [s, c]

    # print("###")
    fin = 0
    for i in range(10**6-1, -1, -1):
        if Directions[i] != -2:
            fin = i+1
            break

    IS_LOCAL = True

    if IS_LOCAL:
        with open("./out/0000.out", "w") as f:
            print(fin)
            f.write(str(fin) + "\n")
            for i in range(fin):
                if Directions[i] == -2:
                    print(-2)
                    f.write(str(-2) + "\n")
                else:
                    print(*Directions[i])
                    f.write(str(Directions[i][0]) + " " + str(Directions[i][1]) + "\n")

    else:
        print(fin)
        for i in range(fin):
            if Directions[i] == -2:
                print(-2)
            else:
                print(*Directions[i])


if __name__ == "__main__":
    main()
