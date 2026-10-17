"""問題固有の状態を切り離した探索骨格。
出典: AHC042/main.py, AHC027/main2.py, Othello/main.py。PyPy向け。
時間計測や乱数のグローバル状態を変更しない。幅・深さ・反復回数は呼び出し側が指定。
"""

from heapq import nlargest


def beam_search(initial, expand, score, key, width, steps):
    """各深さでscore最大のwidth状態を残す。expand(state)は新しい状態の列。
    key(state)は重複排除用hashable値。終端状態はexpandが空列なら保持する。
    各層の生成候補数をCとしてO(steps*C log width)。最終層の最良状態を返す。
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
    """決定的な交互着手・零和ゲーム。evaluateは手番側視点。O(b^depth)、再帰深さdepth。
    playは元の状態を変更せず次状態を返す。パスがあるゲームはmovesにパスを含める。
    戻り値(評価値, 最善手)。終端/深さ0の手はNone。
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
    """O(n²)の近傍法。distanceは完全な距離行列。巡回順（始点を末尾にも含む）。"""
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
    """対称距離専用。1回O(n²)、最大passes回。入力tourを変更しない。"""
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
