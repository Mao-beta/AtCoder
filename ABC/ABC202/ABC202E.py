import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()



def main():
    """
    PyPyでは通らず、Pythonなら通る
    """
    N = NI()
    P = NLI()
    Q = NI()
    UD = [NLI() for _ in range(Q)]

    graph = [[] for _ in range(N)]
    for i, p in enumerate(P, start=1):
        p -= 1
        #graph[i].append(p)
        graph[p].append(i)

    # クエリiにおけるuに入ったときのdのカウント
    Cin = [0] * Q
    # uにかかわるクエリ番号と対象の深さを保持
    UtoQ = [[] for _ in range(N)]
    for i, (u, d) in enumerate(UD):
        u -= 1
        UtoQ[u].append((i, d))

    # ノードiの深さ
    Depth = [0] * N
    # 今まで見た深さiのノードの数
    Cdepth = [0] * N

    ans = [0] * Q

    def dfs(now):
        now_depth = Depth[now]
        #print("in", now, now_depth)

        IDs = UtoQ[now]
        for i, d in IDs:
            Cin[i] = Cdepth[d]
        #print(IDs, Cin)

        Cdepth[now_depth] += 1
        #print(Cdepth)

        for goto in graph[now]:
            if goto == P[now]-1:
                continue
            Depth[goto] = now_depth + 1
            dfs(goto)

        #print("out", now, now_depth)
        IDs = UtoQ[now]
        for i, d in IDs:
            ans[i] = Cdepth[d] - Cin[i]
        #print(now, IDs, ans)

    dfs(0)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
