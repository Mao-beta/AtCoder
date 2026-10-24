"""非再帰重心分解。無向木を入力し分解木を得る。O(n log n)。

抽出元: ABC/ABC291/ABC291H.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    cd = CentroidDecomposition(3, [[1], [0, 2], [1]])
    cd.cd_parents  # => [1, -1, 1]
"""

from collections import deque


class CentroidDecomposition:
    """N頂点の無向木の隣接リストG（0-indexed）を重心分解する。
    cd_parents[v]は重心分解木での親。唯一の根は-1。元の木の親ではない。
    構築O(N log N)、非再帰。分解後の距離集計などは呼び出し側で実装する。
    入力: Nは頂点数、Gは長さNの隣接リストG[u]=[v,...]。0-indexedの連結無向木で各辺を両方向に入れる。構築O(N log(N+1))時間・O(N)空間。
    """

    def __init__(self, N, G):
        """入力: Nは頂点数、Gは長さNの隣接リストG[u]=[v,...]。0-indexedの連結無向木で各辺を両方向に入れる。構築O(N log(N+1))時間・O(N)空間。
        """
        self.N = N
        self.G = G
        self.subsizes = [0] * N
        self.is_removed = [0] * N
        self.cd_parents = [-1] * N  # 分解後の親

        self._build()

    def _build(self):
        if self.N == 0:
            return
        # ある部分木について探索開始する点、サイズ、前回のcentroid
        roots = deque([[0, self.N, -1]])

        while roots:
            root, total, cd_par = roots.popleft()

            # 部分木の中でDFS
            stack = deque()
            stack.append([~root, -1])
            stack.append([root, -1])

            while stack:
                # print(stack)
                now, par = stack.pop()

                # 行きがけ
                if now >= 0:
                    # print("now", now)
                    self.subsizes[now] = 1

                    for goto in self.G[now]:
                        if goto == par or self.is_removed[goto]:
                            continue

                        stack.append([~goto, now])
                        stack.append([goto, now])

                # 帰りがけ
                else:
                    now = ~now
                    # 親のサイズに自分のサイズを加算
                    if par != -1:
                        self.subsizes[par] += self.subsizes[now]

                    # 自分を根としたときの部分木サイズの最大が、合計サイズの半分以下なら重心
                    subsize_max = -1
                    for goto in self.G[now]:
                        if goto == par or self.is_removed[goto]:
                            continue
                        subsize_max = max(subsize_max, self.subsizes[goto])

                    subsize_max = max(subsize_max, total - self.subsizes[now])

                    # 重心だったら新たなrootを追加
                    if subsize_max <= total // 2:
                        # 親の部分木サイズを便宜的に処理（自分を根としたときのサイズ）
                        if par != -1:
                            self.subsizes[par] = total - self.subsizes[now]

                        self.cd_parents[now] = cd_par
                        self.is_removed[now] = 1
                        for goto in self.G[now]:
                            if self.is_removed[goto]:
                                continue
                            # 自分の隣接点を新たな探索開始点とし、そのサイズはsubsizes[goto]
                            roots.append([goto, self.subsizes[goto], now])
                        break
