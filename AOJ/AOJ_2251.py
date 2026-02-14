import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


class mf_graph:
    '''
    燃やす埋める: S → A/B → G, S → Aを切るならS → Bも切る は A → B(inf)
    最小流量制限: A → B(Lt ～ Rt)
    A → B(Rt - Lt), St2 → B(Lt), A → Gl2(Lt) の辺を代わりに張る。
    St2 → Gl2, St2 → Gl, St → Gl2, St → Gl の順に流し、St2, Gl2の辺がcap = 0ならOK
    ---
    G[now]: (頂点nowに起始する辺番号)の二次元配列を回避し、定数倍高速化を目指します。
    順辺の個数は self.M で取得できます。
    '''

    def __init__(self, N: int, inf='4 * 10 ** 18'):
        # edge[i << 1], edge[i << 1 | 1]: i個目の「順辺」のnow, nxt
        # cap[i]: 辺iの容量
        # post[i] : 辺番号iの起始をnowとしたとき、nowの前の辺番号
        #          二次元配列との対比: G[now] = [･･･, post[i], i, ･･･]
        # base[now] : 頂点nowのイテレート開始辺  len(G[now]) == 0の場合、-1
        self.N = N
        self.M = 0
        self.inf = max(0, inf) if type(inf) != str else 4 * 10 ** 18
        self._edge = []
        self._cap = []
        self._post = []
        self._base = [-1] * N

        # 最大流計算でのみ使う配列もあらかじめ宣言する
        self._dist, self._flow, self._leak = [N] * N, [0] * N, [0] * N
        self._arrow, self._queue_and_stack = [-1] * N, [0] * N

    # 最大流計算 主要部を内部関数化
    def _calc(self, St, Gl, permissible_error, flow_limit):
        # dist[now]: StからのBFS上の最短距離
        # flow[now], leak[now]: 頂点nowに流入したフロー・流出が確定したフロー
        # arrow[now] : 頂点nowがちょうど今見ている辺番号
        # queue, stack: 同一配列を参照  BFSではdequeの代用  DFSでは非再帰化に用いる
        N = self.N
        edge, cap, post, base = self._edge, self._cap, self._post, self._base
        dist = self._dist
        flow = self._flow
        leak = self._leak
        arrow = self._arrow
        queue = stack = self._queue_and_stack
        flow_limit = max(0, flow_limit) if type(flow_limit) != str else self.inf
        pe = max(0, permissible_error)  # 許容誤差
        ans = 0

        # Dual-Primal step
        while flow_limit > ans:
            # Phase 1. BFS
            for now in range(N):  # 初期化
                dist[now] = N
            dist[St] = 0
            queue[Rt := 0] = St
            for Lt, now in enumerate(queue):
                arrow[now] = base[now]  # BFS出現辺のみarrow[now]を初期化すると定数倍改善
                x = dist[now] + 1  # 次の距離

                # now → nxtの辺を列挙
                i = base[now]
                while i != -1:
                    # 容量が有意に残る辺で、かつBFS未到達ならキューに入れる
                    if cap[i] > pe and dist[nxt := edge[i ^ 1]] == N:
                        dist[nxt] = x
                        queue[Rt := Rt + 1] = nxt
                    i = post[i]
                if Lt == Rt or now == Gl:
                    break

            if dist[Gl] == N:  # St → Glの辺がない場合、終了
                break

            # Phase 2. St ← Gl方向にDFS
            flow[Gl] = flow_limit - ans  # 流せる総量(基本的にinf)
            leak[Gl] = 0
            stack[d := 0] = Gl
            while True:
                # 1. DFSがGl(DFS開始点)に戻ってきた段階で、残フローをすべて使い切れた場合
                if (now := stack[d]) == Gl and flow[Gl] == leak[Gl]:
                    return ans + leak[Gl]  # 全部流せたと報告し、DFSを打ち切る

                # 2. 目的地Stに到達するか、これ以上流せない場合
                if now == St or flow[now] == leak[now]:
                    # (St側) → now → back → (Gl側) の順に頂点backを定義する。
                    # 流量 f := flow[now]  すなわち 届いたフロー全部 を流す
                    # now ← back は(backから見た)順辺i。 now → backは逆辺となるのでi ^ 1
                    back = stack[d := d - 1]
                    f = flow[now]
                    cap[i := arrow[back]] += f  # 逆辺容量を変更
                    cap[i ^ 1] -= f
                    leak[back] += f  # ひとつ前の頂点の流出量を反映
                    continue

                # 3. (St側) → nxt → now → (Gl側) の順に頂点nxtを定義する。
                #   フローの本来の向きは探索順の逆で、 nxt → now なので注意
                #   なのでDFS上では残容量のある、(nowから見た)逆辺を探すことになる
                x = dist[now] - 1  # 次の距離
                while (i := arrow[now]) != -1:
                    if dist[nxt := edge[i ^ 1]] == x and (rev_cap := cap[i ^ 1]) > pe:
                        # 次の頂点に入るときにはじめてflow[nxt], leak[nxt]を更新
                        flow[nxt] = min(flow[now] - leak[now], rev_cap)
                        leak[nxt] = 0
                        stack[d := d + 1] = nxt
                        break  # ここでは辺番号を変更しない。帰りがけの処理時に変えてもらう
                    else:
                        arrow[now] = post[i]

                # 4. 帰りがけの処理
                else:
                    assert arrow[now] == -1
                    if now == Gl:  # このDFSを終える処理
                        assert d == 0
                        ans += leak[now]
                        break  # DFS終了

                    # (St側) → now → back → (Gl側) の順に頂点backを定義する。
                    # now → back に流量leak[now] : 流れることが決まったフロー総量 を流す
                    # その後、この辺の削除操作を行う( A[back]を変える )
                    back = stack[d := d - 1]
                    cap[i := arrow[back]] -= (f := leak[now])
                    cap[i ^ 1] += f
                    leak[back] += f
                    arrow[back] = post[i]

        # dual-primal stepが終了したのでansを出力
        return ans

    # 辺の追加
    def add_edge(self, From: int, To: int, Cap):
        assert From in range(self.N) and To in range(self.N) and 0 <= Cap
        self._post.append(len(self._edge));
        self._edge.append(From);
        self._cap.append(Cap)
        self._post.append(len(self._edge));
        self._edge.append(To);
        self._cap.append(0)
        self._base[From], self._post[-2] = self._post[-2], self._base[From]
        self._base[To], self._post[-1] = self._post[-1], self._base[To]
        self.M += 1

    def get_edge(self, i: int):  # i番目の順辺の now, nxt, cap(順辺), rev_cap(逆辺)
        assert i in range(self.M)
        fw, rv = i << 1, i << 1 | 1
        return self._edge[fw], self._edge[rv], self._cap[fw], self._cap[rv]

    # 最大流を計算  許容誤差: 残余容量がper_error以下の辺は容量0とみなす
    def calc(self, start: int, goal: int, permissible_error=0, flow_limit='infinity'):
        assert start in range(self.N) and goal in range(self.N) and start != goal
        return self._calc(start, goal, permissible_error, flow_limit)

    # 辺容量がすべて整数の場合に限り、O(NMlogC)で解ける
    def calc_int(self, start: int, goal: int,
                 max_capacity: int = 'infinity', flow_limit='infinity'):
        assert start in range(self.N) and goal in range(self.N) and start != goal
        m = max_capacity if type(max_capacity) != str else round(self.inf)
        f = flow_limit if type(flow_limit) != str else round(self.inf)

        # 容量スケーリングの開始点を決める
        m = min(m, f)
        logm = max(1, round(m)).bit_length() - 1
        ans = 0

        # 容量が(1 << e)以上の辺のみを使う → (1 << e) - 1より真に大きい辺のみを使う
        for e in range(logm, -1, -1):
            ans += self._calc(start, goal, (1 << e) - 1, f - ans)
        return ans

    # St → Glに最大流を流し終えた状態を仮定する。最小カットのSt側頂点かの判定フラグを返す
    def min_cut(self, St, permissible_error=0):
        assert St in range(self.N)
        pe = max(0, permissible_error)  # 許容誤差
        visited = [False] * self.N
        visited[St] = True
        queue = self._queue_and_stack
        queue[Rt := 0] = St
        for Lt, now in enumerate(queue):
            i = self._base[now]
            while i != -1:
                if self._cap[i] > pe and visited[nxt := self._edge[i ^ 1]] == False:
                    visited[nxt] = True
                    queue[Rt := Rt + 1] = nxt
                i = self._post[i]
            if Lt == Rt:
                break
        return visited


def main():
    while True:
        N, M, L = NMI()
        if N == 0 and M == 0 and L == 0:
            return

        UVD = EI(M)
        PT = EI(L)
        PT.sort(key=lambda x: x[1])

        G = mf_graph(2 * L + 2)
        S = 2 * L
        T = S + 1

        INF = 10**15
        D = [[INF]*N for _ in range(N)]
        for i in range(N):
            D[i][i] = 0

        for u, v, d in UVD:
            D[u][v] = d
            D[v][u] = d
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])

        for i in range(L):
            pi, ti = PT[i]
            G.add_edge(S, i, 1)
            G.add_edge(i+L, T, 1)
            for j in range(i+1, L):
                pj, tj = PT[j]
                if tj-ti >= D[pi][pj]:
                    G.add_edge(i, j+L, 1)

        f = G.calc(S, T)
        print(L-f)


if __name__ == "__main__":
    main()
