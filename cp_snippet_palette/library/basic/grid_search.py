"""グリッドの複数始点BFS・最短路復元・4/8近傍成分・最小方向転換回数。
座標は0-indexedの(row,column)。gridは同じ長さの文字列のlist、変更しない。
各関数O(HW)時間・空間。標準Pythonのみ、Codonコンパイル未確認。

使い方（このファイル全体を貼り付けてから実行）
    grid = ['..#', '...', '#..']
    grid_bfs(grid, [(0, 0)])[2][2]  # => 4
    path = grid_shortest_path(grid, (0, 0), (2, 2))
    len(path), path[0], path[-1]  # => (5, (0, 0), (2, 2))
    grid_min_turns(grid, (0, 0), (2, 2))  # => 2
    grid_components(['#.', '.#'], filled='#', diagonal=True)[1]  # => [2]
"""

from collections import deque


def _grid_shape(grid):
    h, w = len(grid), len(grid[0]) if grid else 0
    assert all(len(row) == w for row in grid)
    return h, w


def grid_bfs(grid, sources, wall="#"):
    """複数始点からの4近傍最短距離をH×Wのlistで返す。未到達・壁は-1。
    sources=[(r,c),...]、壁の始点は無視。同じ始点の重複可。O(HW)。
    入力: gridは同じ長さのstrの列、または長方形の二次元列。H=len(grid)、W=len(grid[0])。座標は0-indexedの(row,col)。
    時間・空間O(HW)。
    wallは通行不可セルの値。sourcesはグリッド内の始点座標の列。始点数Sの読み込みも含めるとO(HW+S)時間。
    """
    h, w = _grid_shape(grid)
    dist, queue = [[-1] * w for _ in range(h)], deque()
    for r, c in sources:
        assert 0 <= r < h and 0 <= c < w
        if grid[r][c] != wall and dist[r][c] < 0:
            dist[r][c] = 0
            queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (
                0 <= nr < h
                and 0 <= nc < w
                and grid[nr][nc] != wall
                and dist[nr][nc] < 0
            ):
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist


def grid_shortest_path(grid, start, goal, wall="#"):
    """4近傍最短路の座標list（両端を含む）。到達不能ならNone。O(HW)。
    入力: gridは同じ長さのstrの列、または長方形の二次元列。H=len(grid)、W=len(grid[0])。座標は0-indexedの(row,col)。
    時間・空間O(HW)。
    start/goalは始点/終点の座標tuple。wallは通行不可セルの値（既定は文字#）。
    """
    dist = grid_bfs(grid, [start], wall)
    r, c = goal
    assert 0 <= r < len(grid) and 0 <= c < len(grid[0])
    if dist[r][c] < 0:
        return None
    result = [(r, c)]
    while (r, c) != start:
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and dist[nr][nc] == dist[r][c] - 1
            ):
                r, c = nr, nc
                result.append((r, c))
                break
    return result[::-1]


def grid_components(grid, filled="#", diagonal=False):
    """filledのマスの(成分IDの二次元list,成分サイズlist)。対象外ID=-1。
    diagonal=Falseなら4近傍、Trueなら8近傍。各成分IDは行優先の発見順。O(HW)。
    入力: gridは同じ長さのstrの列、または長方形の二次元列。H=len(grid)、W=len(grid[0])。座標は0-indexedの(row,col)。
    時間・空間O(HW)。
    filledは連結成分に含めるセルの値。diagonalは斜め隣接も許すかを表すbool。
    """
    h, w = _grid_shape(grid)
    ids, sizes = [[-1] * w for _ in range(h)], []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] != filled or ids[r][c] >= 0:
                continue
            ids[r][c] = len(sizes)
            queue, count = deque([(r, c)]), 0
            while queue:
                y, x = queue.popleft()
                count += 1
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if (
                        0 <= ny < h
                        and 0 <= nx < w
                        and grid[ny][nx] == filled
                        and ids[ny][nx] < 0
                    ):
                        ids[ny][nx] = len(sizes)
                        queue.append((ny, nx))
            sizes.append(count)
    return ids, sizes


def grid_min_turns(grid, start, goal, wall="#"):
    """4近傍で移動する際の最小方向転換回数。最初の方向は自由。到達不能は-1。
    (マス,直前の方向)を状態にした0-1 BFS。O(HW)時間・空間。
    入力: gridは同じ長さのstrの列、または長方形の二次元列。H=len(grid)、W=len(grid[0])。座標は0-indexedの(row,col)。
    時間・空間O(HW)。
    start/goalは始点/終点の座標tuple。wallは通行不可セルの値（既定は文字#）。
    """
    h, w = _grid_shape(grid)
    sr, sc = start
    gr, gc = goal
    assert 0 <= sr < h and 0 <= sc < w and 0 <= gr < h and 0 <= gc < w
    if grid[sr][sc] == wall or grid[gr][gc] == wall:
        return -1
    inf = 4 * h * w + 1
    dist = [[inf] * 4 for _ in range(h * w)]
    initial = sr * w + sc
    dist[initial] = [0] * 4
    queue = deque((initial, d, 0) for d in range(4))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        v, direction, cost = queue.popleft()
        if cost != dist[v][direction]:
            continue
        r, c = divmod(v, w)
        if (r, c) == goal:
            return cost
        for nd, (dy, dx) in enumerate(directions):
            nr, nc = r + dy, c + dx
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != wall:
                to, extra = nr * w + nc, nd != direction
                if cost + extra < dist[to][nd]:
                    dist[to][nd] = cost + extra
                    state = (to, nd, cost + extra)
                    if extra:
                        queue.append(state)
                    else:
                        queue.appendleft(state)
    return -1
