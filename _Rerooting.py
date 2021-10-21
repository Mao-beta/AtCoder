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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res



class Rerooting:
    """
    抽象化全方位木DP merge, op, ide_eleを差し替えて使える
    """
    def __init__(self, N, merge, op, ide_ele):
        self.N = N

        ### 問題ごとに変更する
        # 子同士の二項演算　モノイド
        self.merge = merge
        # 二項演算前のdpの値への補正
        self.op = op
        # mergeに関する単位元
        self.ide_ele = ide_ele
        ### ここまで

        self.graph = [[] for _ in range(N)]
        self.parents = [self.N] * self.N
        self.dp = [self.ide_ele] * self.N

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def calc(self):
        self.dfs1(0)
        ans = self.dfs2()
        return ans

    def dfs1(self, root):
        # rootが固定のときの木DP
        # dfs帰りがけ順に処理
        self.root = root
        stack = deque()
        stack.append(root)

        while stack:
            now = stack.pop()

            # 行きがけ
            if now >= 0:
                stack.append(~now)
                for goto in self.graph[now]:
                    if goto == self.parents[now]:
                        continue
                    self.parents[goto] = now
                    stack.append(goto)

            # 帰りがけ
            # 親以外の隣接点に関して遷移
            else:
                now = ~now
                for goto in self.graph[now]:
                    if goto == self.parents[now]:
                        continue
                    self.dp[now] = self.merge(self.dp[now], self.op(self.dp[goto]))

    def dfs2(self):
        # Rerooting
        # 根を移動させたときの、
        # 移動前の点以下の部分木に関する値を更新してdpに入れる
        # その値は移動後の点以外のmerge(dp[c])なので、これの累積をとっておく
        # 移動後の根に来たら、移動前の点からの情報(dp_p)も受け取り、
        # 子のdpの値と一緒に処理する

        ans = [self.ide_ele] * self.N
        stack = deque()
        stack.append((self.root, self.ide_ele))

        while stack:
            now, dp_p = stack.pop()

            mul_l = [1]
            for goto in self.graph[now]:
                if goto == self.parents[now]:
                    mul_l.append(self.merge(mul_l[-1], self.op(dp_p)))
                else:
                    mul_l.append(self.merge(mul_l[-1], self.op(self.dp[goto])))

            mul_r = [1]
            for goto in self.graph[now][::-1]:
                if goto == self.parents[now]:
                    mul_r.append(self.merge(mul_r[-1], self.op(dp_p)))
                else:
                    mul_r.append(self.merge(mul_r[-1], self.op(self.dp[goto])))
            mul_r = mul_r[::-1]

            for i, goto in enumerate(self.graph[now]):
                if goto == self.parents[now]:
                    ans[now] = self.merge(ans[now], self.op(dp_p))
                    continue
                mul = self.merge(mul_l[i], mul_r[i + 1])
                ans[now] = self.merge(ans[now], self.op(self.dp[goto]))
                stack.append((goto, mul))

        return ans


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(N-1)]

    ### 問題ごとに変更する
    # 子同士の二項演算　モノイド
    merge = lambda a, b: a * b % M
    # 二項演算前のdpの値への補正
    op = lambda a: a + 1
    # mergeに関する単位元
    ide_ele = 1

    tree = Rerooting(N, merge, op, ide_ele)
    for x, y in edges:
        tree.add_edge(x-1, y-1)
        tree.add_edge(y-1, x-1)
    ans = tree.calc()

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
