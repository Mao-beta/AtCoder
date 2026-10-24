"""問題固有の状態を切り離した探索骨格。

出典: AHC042/main.py, AHC027/main2.py, Othello/main.py。PyPy向け。

時間計測や乱数のグローバル状態を変更しない。幅・深さ・反復回数は呼び出し側が指定。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    beam_search(0, lambda s: [s+1, s+2], lambda s: s, lambda s: s, width=2, steps=3)  # => 6

残り1個か2個を取れる石取りゲーム。最後を取った側が勝ち。
    moves = lambda n: range(1, min(n, 2) + 1)
    value, move = negamax(2, 2, moves, lambda n, k: n-k, lambda n: -1 if n == 0 else 0, lambda n: n == 0)
    value, move  # => (1, 2)
    distance = [[0, 2, 4], [2, 0, 3], [4, 3, 0]]
    tour = tsp_nearest_neighbor(distance)
    tour, tsp_two_opt(distance, tour)  # => ([0, 1, 2, 0], [0, 1, 2, 0])
"""

from heapq import nlargest


def beam_search(initial, expand, score, key, width, steps):
    """各深さでscore最大のwidth状態を残す。expand(state)は新しい状態の列。
    key(state)は重複排除用hashable値。終端状態はexpandが空列なら保持する。
    各層の生成候補数をCとしてO(steps*C log width)。最終層の最良状態を返す。
    initialは初期状態。expand/score/keyは状態を受け取る関数で、scoreは比較可能な評価値、keyは同値状態をまとめるhashable値を返す。
    widthは正の整数の残す幅、stepsは非負整数の探索段数。空間O(C+width)個の状態（状態自体の容量は別）。
    """
    if width <= 0 or steps < 0:
        raise ValueError("positive width and nonnegative steps required")
    beam = [initial]
    for _ in range(steps):
        candidates = {}
        for state in beam:
            children = list(expand(state))
            for child in children if children else [state]:
                signature = key(child)
                value = score(child)
                if signature not in candidates or candidates[signature][0] < value:
                    candidates[signature] = (value, child)
        beam = [
            item[1]
            for item in nlargest(width, candidates.values(), key=lambda item: item[0])
        ]
    return max(beam, key=score)


def negamax(
    state,
    depth,
    moves,
    play,
    evaluate,
    terminal,
    alpha=float("-inf"),
    beta=float("inf"),
):
    """交互着手・零和ゲームで(手番側の評価値,最善手)を返す。深さ制限付きαβ探索。
    moves(state)は合法手の列、play(state,move)は元状態を変えず次状態を返す。
    evaluate(state)は現在の手番側視点の値、terminal(state)は終了判定のbool。
    終端/深さ0/合法手なしなら手はNone。パスはmovesで明示する。O(b^depth)。
    stateは初期状態、depthは探索する非負手数。alpha/betaは現在の評価の下限/上限。bは1状態からの最大合法手数。
    コールバックの計算量を除き時間O(b^depth)、作業領域O(depth*b)個の手・状態以内。
    """
    if depth <= 0 or terminal(state):
        return evaluate(state), None
    legal = list(moves(state))
    if not legal:
        return evaluate(state), None
    best, best_move = float("-inf"), legal[0]
    for move in legal:
        value, _ = negamax(
            play(state, move), depth - 1, moves, play, evaluate, terminal, -beta, -alpha
        )
        value = -value
        if value > best:
            best, best_move = value, move
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return best, best_move


def tsp_nearest_neighbor(distance, start=0):
    """O(n²)の近傍法。distanceは完全な距離行列。巡回順（始点を末尾にも含む）。
    distanceはn×nの数値費用行列、n=len(distance)。startは0..n-1の始点。追加空間O(n)。
    """
    n = len(distance)
    if n == 0:
        return []
    if not 0 <= start < n or any(len(row) != n for row in distance):
        raise ValueError("invalid distance matrix or start")
    unused = set(range(n))
    unused.remove(start)
    tour = [start]
    while unused:
        v = min(unused, key=lambda x: (distance[tour[-1]][x], x))
        unused.remove(v)
        tour.append(v)
    return tour + [start]


def tsp_two_opt(distance, tour, passes=10):
    """対称なn×n費用行列distance、長さn+1の閉じた巡回順tour、非負整数passesを入力する。改善した新しい頂点順listを返し、元のtourは変えない。
    1走査O(n²)回の候補評価に加え、採用した反転の長さの総和だけ時間がかかる。最悪O(passes*n³)時間・O(n)空間。最適性は保証しない。
    """
    if passes < 0:
        raise ValueError("negative passes")
    route = list(tour)
    if len(route) <= 3:
        return route
    if route[0] != route[-1]:
        raise ValueError("closed tour required")
    for _ in range(passes):
        changed = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                a, b, c, d = route[i - 1], route[i], route[j], route[j + 1]
                if distance[a][c] + distance[b][d] < distance[a][b] + distance[c][d]:
                    route[i : j + 1] = reversed(route[i : j + 1])
                    changed = True
        if not changed:
            break
    return route
