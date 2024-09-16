import random
import copy

class Othello:
    EMPTY = 0
    BLACK = 1
    WHITE = 2
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 八方向

    def __init__(self):
        self.board = [[self.EMPTY for _ in range(8)] for _ in range(8)]
        self.board[3][3], self.board[3][4] = self.WHITE, self.BLACK
        self.board[4][3], self.board[4][4] = self.BLACK, self.WHITE
        self.pass_count = 0

    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        for row in range(8):
            print(f"{row} " + " ".join(self.symbol(self.board[row][col]) for col in range(8)))
        print()

    @staticmethod
    def symbol(value):
        if value == Othello.BLACK:
            return 'B'
        elif value == Othello.WHITE:
            return 'W'
        else:
            return '.'

    def is_on_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def is_valid_move(self, row, col, color):
        if self.board[row][col] != self.EMPTY or not self.is_on_board(row, col):
            return False

        opponent = Othello.WHITE if color == Othello.BLACK else Othello.BLACK

        for direction in Othello.DIRECTIONS:
            x, y = row, col
            x += direction[0]
            y += direction[1]
            if self.is_on_board(x, y) and self.board[x][y] == opponent:
                x += direction[0]
                y += direction[1]
                if not self.is_on_board(x, y):
                    continue
                while self.is_on_board(x, y) and self.board[x][y] == opponent:
                    x += direction[0]
                    y += direction[1]
                    if not self.is_on_board(x, y):
                        break
                if self.is_on_board(x, y) and self.board[x][y] == color:
                    return True
        return False

    def place_tile(self, row, col, color):
        if not self.is_valid_move(row, col, color):
            return False

        self.board[row][col] = color
        opponent = Othello.WHITE if color == Othello.BLACK else Othello.BLACK
        tiles_to_flip = []

        for direction in Othello.DIRECTIONS:
            x, y = row, col
            x += direction[0]
            y += direction[1]
            if self.is_on_board(x, y) and self.board[x][y] == opponent:
                possible_tiles = []
                while self.is_on_board(x, y) and self.board[x][y] == opponent:
                    possible_tiles.append((x, y))
                    x += direction[0]
                    y += direction[1]
                if self.is_on_board(x, y) and self.board[x][y] == color:
                    tiles_to_flip.extend(possible_tiles)

        for x, y in tiles_to_flip:
            self.board[x][y] = color

        self.pass_count = 0  # 石を置いたらパスカウントをリセット
        return True

    def get_valid_moves(self, color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col, color):
                    valid_moves.append((row, col))
        return valid_moves

    def count_pieces(self):
        black_count = sum(row.count(self.BLACK) for row in self.board)
        white_count = sum(row.count(self.WHITE) for row in self.board)
        return black_count, white_count

    def is_game_over(self):
        black_moves = self.get_valid_moves(self.BLACK)
        white_moves = self.get_valid_moves(self.WHITE)

        if not black_moves and not white_moves:
            # 両者が合法手を持たない（連続パス）
            return True
        elif self.pass_count >= 2:
            # 両者が連続でパスした場合
            return True
        elif all(self.board[row][col] != self.EMPTY for row in range(8) for col in range(8)):
            # 盤面がすべて埋まっている場合
            return True
        return False

    def print_winner(self):
        black_count, white_count = self.count_pieces()
        print(f"最終結果: 黒 {black_count}, 白 {white_count}")
        if black_count > white_count:
            print("黒の勝ちです！")
        elif white_count > black_count:
            print("白の勝ちです！")
        else:
            print("引き分けです！")


    def place_tile_reversible(self, row, col, color):
        """
        置いた手を元に戻すためのリバータブル版。
        この関数は、変更された箇所を記録し、後で元に戻せるようにする。
        """
        if not self.is_valid_move(row, col, color):
            return False, []

        opponent = Othello.WHITE if color == Othello.BLACK else Othello.BLACK
        flipped_tiles = []

        for direction in Othello.DIRECTIONS:
            x, y = row, col
            x += direction[0]
            y += direction[1]
            if self.is_on_board(x, y) and self.board[x][y] == opponent:
                possible_tiles = []
                while self.is_on_board(x, y) and self.board[x][y] == opponent:
                    possible_tiles.append((x, y))
                    x += direction[0]
                    y += direction[1]
                if self.is_on_board(x, y) and self.board[x][y] == color:
                    flipped_tiles.extend(possible_tiles)

        # 変更を適用
        for x, y in flipped_tiles:
            self.board[x][y] = color
        self.board[row][col] = color
        return True, flipped_tiles

    def undo_move(self, row, col, flipped_tiles, original_color):
        """
        リバータブルな操作を元に戻す。
        """
        self.board[row][col] = Othello.EMPTY  # 元の位置を空に戻す
        for x, y in flipped_tiles:
            self.board[x][y] = original_color  # ひっくり返した石を元に戻す

# 評価関数の定義
# 新しい評価関数
# 新しい評価関数にモビリティを追加
# 新しい評価関数に重み付けされたポジション評価を追加
position_weights = [
    [100, -24, 0, -1, -1, 0, -24, 100],
    [-24, -30, -3, -3, -3, -3, -30, -24],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-24, -30, -3, -3, -3, -3, -30, -24],
    [100, -24, 0, -1, -1, 0, -24, 100],
]


def count_stable_discs(board, color):
    """
    確定石を数える関数。盤面の端や角を基準にして確定石を数える。
    """
    stable_discs = 0

    # 左上、右上、左下、右下の角からそれぞれ確定石を数える
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 右, 下, 右下, 左下の4方向をチェック

    for start in [(0, 0), (0, 7), (7, 0), (7, 7)]:  # 各角を基点に調べる
        row, col = start
        if board.board[row][col] == color:
            stable_discs += 1
            for direction in directions:
                r, c = row + direction[0], col + direction[1]
                while board.is_on_board(r, c) and board.board[r][c] == color:
                    stable_discs += 1
                    r += direction[0]
                    c += direction[1]

    return stable_discs


def evaluate(board, color):
    # コマの数
    black_count, white_count = board.count_pieces()
    turn = (black_count + white_count) / 64

    if color == Othello.BLACK:
        piece_difference = black_count - white_count
    else:
        piece_difference = white_count - black_count

    # 位置による重み付け評価
    position_score = 0
    for row in range(8):
        for col in range(8):
            if board.board[row][col] == Othello.BLACK:
                position_score += position_weights[row][col] if color == Othello.BLACK else -position_weights[row][col]
            elif board.board[row][col] == Othello.WHITE:
                position_score -= position_weights[row][col] if color == Othello.BLACK else position_weights[row][col]

    # モビリティ（合法手の数）
    black_mobility = len(board.get_valid_moves(Othello.BLACK))
    white_mobility = len(board.get_valid_moves(Othello.WHITE))
    mobility_score = (black_mobility - white_mobility) if color == Othello.BLACK else (white_mobility - black_mobility)

    # 確定石の数
    black_stable_discs = count_stable_discs(board, Othello.BLACK)
    white_stable_discs = count_stable_discs(board, Othello.WHITE)
    stable_score = (black_stable_discs - white_stable_discs) if color == Othello.BLACK else (
                white_stable_discs - black_stable_discs)

    # 総合評価
    total_score = piece_difference * turn**3 * 64/25 + position_score + mobility_score + stable_score * 3
    return int(total_score)


# 戦略クラスのベース
class Strategy:
    def select_move(self, board, color):
        raise NotImplementedError("This method should be overridden.")

# ランダムな合法手を選ぶ戦略
class RandomStrategy(Strategy):
    def select_move(self, board, color):
        valid_moves = board.get_valid_moves(color)
        if valid_moves:
            return random.choice(valid_moves)
        return None

# Negamax戦略の実装
class NegamaxStrategy(Strategy):
    def __init__(self, depth=1):
        self.depth = depth

    def select_move(self, board, color):
        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            return None

        best_score = -float('inf')
        best_move = None
        for move in valid_moves:
            new_board = self.simulate_move(board, move, color)
            score = -self.negamax(new_board, self.depth - 1, self.opponent(color))
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def negamax(self, board, depth, color):
        if depth == 0 or board.is_game_over():
            return evaluate(board, color)

        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            # パス
            return -self.negamax(board, depth - 1, self.opponent(color))

        max_score = -float('inf')
        for move in valid_moves:
            new_board = self.simulate_move(board, move, color)
            score = -self.negamax(new_board, depth - 1, self.opponent(color))
            if score > max_score:
                max_score = score
        return max_score

    def simulate_move(self, board, move, color):
        new_board = copy.deepcopy(board)
        new_board.place_tile(move[0], move[1], color)
        return new_board

    def opponent(self, color):
        return Othello.WHITE if color == Othello.BLACK else Othello.BLACK


# Negamaxのアルファベータ剪定バージョン
class NegamaxAlphaBetaStrategy(Strategy):
    def __init__(self, depth=1):
        self.depth = depth

    def select_move(self, board, color):
        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            return None

        best_score = -float('inf')
        best_move = None
        alpha = -float('inf')
        beta = float('inf')

        for move in valid_moves:
            row, col = move
            # 仮想的に手を置く
            success, flipped_tiles = board.place_tile_reversible(row, col, color)
            if success:
                score = -self.negamax(board, self.depth - 1, self.opponent(color), -beta, -alpha)
                board.undo_move(row, col, flipped_tiles, self.opponent(color))  # 元に戻す

                if score > best_score:
                    best_score = score
                    best_move = move

                alpha = max(alpha, score)
                if alpha >= beta:
                    break  # 剪定

        return best_move

    def negamax(self, board, depth, color, alpha, beta):
        if depth == 0 or board.is_game_over():
            return evaluate(board, color)

        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            return -self.negamax(board, depth - 1, self.opponent(color), -beta, -alpha)

        max_score = -float('inf')

        for move in valid_moves:
            row, col = move
            success, flipped_tiles = board.place_tile_reversible(row, col, color)
            if success:
                score = -self.negamax(board, depth - 1, self.opponent(color), -beta, -alpha)
                board.undo_move(row, col, flipped_tiles, self.opponent(color))  # 元に戻す

                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break  # 剪定

        return max_score

    def opponent(self, color):
        return Othello.WHITE if color == Othello.BLACK else Othello.BLACK


# 人間プレイヤーの手動入力戦略
class HumanStrategy(Strategy):
    def select_move(self, board, color):
        board.print_board()
        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            print("合法手がありません。パスします。")
            return None

        print(f"あなたは{'黒' if color == Othello.BLACK else '白'}です。合法手: {valid_moves}")
        while True:
            try:
                move = input("行と列をスペース区切りで入力してください (例: 3 2): ")
                row, col = map(int, move.split())
                if (row, col) in valid_moves:
                    return (row, col)
                else:
                    print("その場所には置けません。合法手の中から選んでください。")
            except ValueError:
                print("無効な入力です。もう一度入力してください。")

# AIプレイヤークラス
class OthelloAI:
    def __init__(self, color, strategy):
        self.color = color
        self.strategy = strategy

    def make_move(self, board):
        move = self.strategy.select_move(board, self.color)
        if move:
            board.place_tile(move[0], move[1], self.color)
        return move


# ゲームシミュレーションの例
if __name__ == "__main__":
    othello = Othello()
    othello.print_board()

    # 黒のAIをNegamax戦略で設定（深さ1）
    # black_ai = OthelloAI(Othello.BLACK, HumanStrategy())
    black_ai = OthelloAI(Othello.BLACK, NegamaxAlphaBetaStrategy(depth=5))

    # 白のAIをランダム戦略で設定
    # white_ai = OthelloAI(Othello.WHITE, NegamaxStrategy(depth=3))
    white_ai = OthelloAI(Othello.WHITE, HumanStrategy())
    # white_ai = OthelloAI(Othello.WHITE, NegamaxAlphaBetaStrategy(depth=5))

    # ゲームループ
    while not othello.is_game_over():
        # 黒の手番
        print("黒の手番")
        black_move = black_ai.make_move(othello)
        if black_move:
            print(f"黒が{black_move}に置きました")
        else:
            print("黒はパスしました")
            othello.pass_count += 1
        othello.print_board()

        if othello.is_game_over():
            break

        # 白の手番
        print("白の手番")
        white_move = white_ai.make_move(othello)
        if white_move:
            print(f"白が{white_move}に置きました")
        else:
            print("白はパスしました")
            othello.pass_count += 1
        othello.print_board()

    # 勝敗を表示
    othello.print_winner()
