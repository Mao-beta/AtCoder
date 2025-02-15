import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())

# グローバル変数：N, POW3（長さ N のリスト：pow3[i] = 3^(N-1-i)）
N = NI()  # 固定で20と想定
# POW3[i] = 3^(N-1-i)
POW3 = [1] * N
for i in range(N-1, -1, -1):
    if i == N-1:
        POW3[i] = 1
    else:
        POW3[i] = POW3[i+1] * 3

# マッピング文字→数字
CHAR2NUM = {'.': 0, 'x': 1, 'o': 2}
NUM2CHAR = {0: '.', 1: 'x', 2: 'o'}
# move のマッピング：0:"L", 1:"R", 2:"U", 3:"D"
MOVE2STR = {0: "L", 1: "R", 2: "U", 3: "D"}

# 入力された各行（文字列）を 3 進数の整数に変換
def row_to_int(row_str):
    val = 0
    for ch in row_str:
        val = val * 3 + CHAR2NUM[ch]
    return val

# ─── BoardState クラス ───
class BoardState:
    __slots__ = ('board', 'moves', 'N')
    def __init__(self, board, moves=None):
        # board: tuple of ints, 各 int は 1 行を 3進数で表現（各行は長さ N）
        # moves: list of int（各 move は d*N + idx）
        self.board = board  # 例: (row0, row1, ..., row_{N-1})
        self.N = len(board)
        self.moves = moves if moves is not None else []

    def hash_val(self):
        # 各行は 32bit 以下 (3^20 < 2^32) なので、各行を 32bit 左シフトで連結
        h = 0
        for row in self.board:
            h = (h << 32) | row
        return h

    def count_ghosts(self):
        cnt = 0
        for row in self.board:
            # 盤面の各行を 3 進数表現から桁ごとに調べる
            # ※ N=20 固定なので、単純に str() に変換するよりループで調べるほうが速い
            # ここではシンプルに、各桁を POW3 を用いて求める
            temp = row
            for _ in range(self.N):
                cnt += 1 if (temp % 3) == 1 else 0
                temp //= 3
        return cnt

    def simulate_move(self, move):
        """
        move: (d, idx)  d in {0,1,2,3}、idx は行番号（d=0,1の場合）または列番号（d=2,3の場合）
        行シフトの場合は、対象行のみ更新します。
        列シフトの場合は、すべての行の該当桁を更新します。
        もし「削除されるセル」が福 (数字 2) なら、その操作は不許可として None を返す。
        """
        d, idx = move
        new_board = list(self.board)  # コピー（各要素は int、immutableなので shallow copyでOK）
        if d == 0:  # "L" : 行 idx を左シフト
            row_val = new_board[idx]
            msd = row_val // POW3[0]  # 最上位桁
            if msd == 2:
                return None
            # 削除される桁を除去し、右端に 0 を追加
            new_row = (row_val % POW3[0]) * 3
            new_board[idx] = new_row
        elif d == 1:  # "R" : 行 idx を右シフト
            row_val = new_board[idx]
            if row_val % 3 == 2:
                return None
            new_row = row_val // 3
            new_board[idx] = new_row
        elif d == 2:  # "U" : 列 idx を上にシフト
            # まず、削除されるセル：行0 の桁 idx
            digit = (new_board[0] // POW3[idx]) % 3
            if digit == 2:
                return None
            # 各行 i (0<=i<=N-2) に対して、新しい桁はもとの行 i+1 の同桁
            for i in range(0, self.N - 1):
                old_digit = (new_board[i] // POW3[idx]) % 3
                new_digit = (self.board[i+1] // POW3[idx]) % 3  # 注意：self.board[i+1]を用いることで元の値を参照
                new_board[i] = new_board[i] - old_digit * POW3[idx] + new_digit * POW3[idx]
            # 最終行の桁 idx は 0 に
            old_digit = (new_board[self.N - 1] // POW3[idx]) % 3
            new_board[self.N - 1] = new_board[self.N - 1] - old_digit * POW3[idx]  # +0
        elif d == 3:  # "D" : 列 idx を下にシフト
            digit = (new_board[self.N - 1] // POW3[idx]) % 3
            if digit == 2:
                return None
            for i in range(self.N - 1, 0, -1):
                old_digit = (new_board[i] // POW3[idx]) % 3
                new_digit = (self.board[i-1] // POW3[idx]) % 3
                new_board[i] = new_board[i] - old_digit * POW3[idx] + new_digit * POW3[idx]
            old_digit = (new_board[0] // POW3[idx]) % 3
            new_board[0] = new_board[0] - old_digit * POW3[idx]  # 0 に
        else:
            return None
        # 新たな状態の moves は、元の moves にこの move を整数で追加（move = d * N + idx）
        new_moves = self.moves + [d * self.N + idx]
        return BoardState(tuple(new_board), new_moves)

    def greedy_completion_cost(self):
        """
        各行について、もしその行に鬼があれば、
          cost_row = min( 2*(max_index + 1), 2*(N - min_index) )
        （ここで max_index, min_index は、その行で鬼が出現する列番号の最大・最小）
        各列についても同様に計算し、行方向と列方向の総和のうち小さいほうを返す。
        """
        total_row = 0
        for row_val in self.board:
            ghost_positions = []
            temp = row_val
            # 20 桁の 3 進数とみなす（左側桁から順に）
            for j in range(self.N):
                # j番目のセル（左から j 番目）は、桁インデックス j であり、対応する重みは POW3[j]
                digit = (row_val // POW3[j]) % 3
                if digit == 1:
                    ghost_positions.append(j)
            if ghost_positions:
                total_row += min(2 * (max(ghost_positions) + 1), 2 * (self.N - min(ghost_positions)))
        total_col = 0
        for j in range(self.N):
            ghost_positions = []
            for i in range(self.N):
                row_val = self.board[i]
                digit = (row_val // POW3[j]) % 3
                if digit == 1:
                    ghost_positions.append(i)
            if ghost_positions:
                total_col += min(2 * (max(ghost_positions) + 1), 2 * (self.N - min(ghost_positions)))
        return min(total_row, total_col)

    def heuristic(self):
        return len(self.moves) + self.greedy_completion_cost()

# ─── BeamSearch クラス ───
class BeamSearch:
    def __init__(self, initial_state, beam_width=50):
        self.initial_state = initial_state
        self.beam_width = beam_width
        self.visited = {}  # key: board_hash (int)  → cost (move数)

    def search(self):
        beam = [self.initial_state]
        best_state = self.initial_state
        while beam:
            next_beam = []
            for state in beam:
                if state.count_ghosts() == 0:
                    return state  # 全鬼除去
                # 候補生成：各行（鬼があるなら）で左右移動、各列（鬼があるなら）で上下移動
                candidates = []
                for i in range(state.N):
                    # 各行を state.board[i] （int）
                    # 鬼があるかは、1 が出るかどうかをチェック
                    # ここでは、str.count を使わず、簡単に「'x'」があるかは、下記のように
                    if state.board[i] != 0 and any(((state.board[i] // POW3[j]) % 3) == 1 for j in range(state.N)):
                        candidates.append((0, i))  # L
                        candidates.append((1, i))  # R
                for j in range(state.N):
                    col_has = False
                    for i in range(state.N):
                        if ((state.board[i] // POW3[j]) % 3) == 1:
                            col_has = True
                            break
                    if col_has:
                        candidates.append((2, j))  # U
                        candidates.append((3, j))  # D
                candidates = set(candidates)
                for cand in candidates:
                    new_state = state.simulate_move(cand)
                    if new_state is None:
                        continue
                    key = self._hash_board(new_state.board)
                    cost = len(new_state.moves)
                    if key in self.visited and self.visited[key] <= cost:
                        continue
                    self.visited[key] = cost
                    next_beam.append(new_state)
            if not next_beam:
                break
            next_beam.sort(key=lambda s: s.heuristic())
            beam = next_beam[:self.beam_width]
        return best_state

    def _hash_board(self, board):
        # board は tuple of ints, 各行は 32bit 以下。各行を 32bit 左シフトで連結
        h = 0
        for row in board:
            h = (h << 32) | row
        return h

# ─── main 関数 ───
def main():
    global N, POW3
    # N はすでに読み込み済み（固定で20）
    board_lines = [input() for _ in range(N)]
    board_ints = tuple(row_to_int(line) for line in board_lines)
    initial_state = BoardState(board_ints)
    beam = BeamSearch(initial_state, beam_width=10)
    best_state = beam.search()
    # 出力：各 move を整数から "L i" などに変換
    out_lines = []
    for m in best_state.moves:
        d = m // N
        idx = m % N
        out_lines.append(f"{MOVE2STR[d]} {idx}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
