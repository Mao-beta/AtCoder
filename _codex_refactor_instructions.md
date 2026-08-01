# Codex向け指示書: AtCoder用ライブラリの再編・検証・高速化

## 0. 背景と前提(必読)

- このリポジトリは AtCoder の解答置き場。ルートおよび `ABC/`, `ARC/`, `yuki/` 等のコンテスト解答ファイル(約4,400本)は**使い捨てであり一切変更禁止**。作業対象はルートの `_*.py`(汎用ライブラリ、約30本・計8,090行)のみ。
- 実行環境は **AtCoder ジャッジの PyPy3**。CPython 前提の最適化(numpy等)は不可。判断に迷う速度特性は必ず PyPy でベンチして決めること。
- 運用スタイルは「**ライブラリファイルからコンテストファイルへ貼り付け**」。import 運用ではない。したがって:
  - 各クラス/関数はコピペで自己完結すること(ファイル内の他定義への暗黙依存を作らない。依存する場合は「※要: XXX も併せて貼る」と docstring に明記)。
  - ファイル分割よりも「1ファイル内でブロックが明確に区切られていること」が重要。
- 目標構成は「**カテゴリ別の大きめファイル**」(現行の `_Graph_Algorithm.py` 方式を踏襲しつつ重複を1箇所に集約)。
- 検証は **Library Checker**(https://judge.yosupo.jp)。既存の `LibraryChecker/` フォルダの形式(1問題1ファイル、標準入出力)を踏襲する。
- 既存の `_atcoder_template.py` の入出力スタイル(`NI/NMI/NLI/SI/SMI/SLI/EI`、`input = lambda: sys.stdin.readline().strip()`)は変えない。ライブラリの引数・返り値もこのスタイルと馴染む形にする。

## 1. 現状インベントリとレビュー結果

### 1.1 重複(統合対象)

| 内容 | 存在箇所 | 備考 |
|---|---|---|
| UnionFind | `_union_find_tree.py`(4変種: UnionFind / WeightedUnionFind / VerDepth / VerSize), `_Data_Structure.py`(UnionFind / WeightedUnionFind) | `_union_find_tree.py` 版は `roots`/`members` を defaultdict(set) で常時保持しており重い(後述) |
| BIT | `_Data_Structure.py`, `_inversion_num.py` | コンテスト側でも81ファイルでほぼ毎回微妙に違う手書き実装 |
| 座標圧縮 compress | `_test.py`, `_inversion_num.py` | コンテスト側83ファイルに複数変種 |
| FFT/畳み込み | `_Convolution.py`(FFT class + FPS), `_FFT_comvolve.py`(typo名), `FPS24*.py` 内の実装群 | FPS24系(2025年)の `ntt/intt/multiply + class FPS` が最新。`_Convolution.py` は2023年版 |
| 幾何 | `_Geometry.py`, `_Geometry_GPT.py` | GPT版の方が網羅的 |
| 平衡木/順序付き集合 | `_AVL_Tree.py`, `_Balancing_Tree.py`, `_Sorted_Set.py`(tatyam版), `_Cpp_Set.py`(**CPython専用**、ファイル内に「PyPyはだめ」と明記あり) | 実戦で使われているのは `_Sorted_Set.py` のみ(SortedMultiset 49ファイル、SortedSet 48ファイルで使用) |
| Dijkstra | `_Graph_Algorithm.py` 内に `Dijkstra` と `__Dijkstra` の2実装 | どちらを正とするか決めて1本化 |

### 1.2 雑多ファイル(再配置対象)

- `_test.py`(684行): 名前に反して実用ユーティリティ置き場になっている。`adjlist`(コンテスト側146ファイルで使用=最頻出)、`compress`、`Doubling`、`Knapsack`、`euler_tour`、グリッド系(`i2hw/hw2i/in_grid`)が埋まっている。
- `_Data_Structure.py`(772行): SegTree, BIT, LCATree, KindDeque, Deque, Heapq ラッパ, SegmentTreeBeats が同居。
- `_Fractions.py`(342行): 名前に反して ModInt, Comb, HugeComb, Eratosthenes, prime_factorize, divisors, 基数変換が同居。
- ツール類(コンテスト補助スクリプト)がライブラリと混在: `_make_contest_files.py`, `_folder_move.py`, `_explain.py`, `_atcoder_template.py`, `_marathon_template.py`。

### 1.3 頻出だが未ライブラリ化 or 埋没しているもの(コンテスト側ファイル数による頻度)

| 頻度 | パターン | 現状 |
|---|---|---|
| 146 | 隣接リスト構築 `adjlist` | `_test.py` に埋没 |
| 123 | UnionFind | ライブラリあり(重複2箇所) |
| 83 | 座標圧縮 | `_test.py`/`_inversion_num.py` に分散、変種多数 |
| 81 | BIT | あり(重複) |
| 69 | 素因数分解 | `_Fractions.py` に prime_factorize/prime_fact の2変種 |
| 68 | 約数列挙 divisors | `_Fractions.py` |
| 64 | Comb(階乗前計算) | `_Fractions.py` だが FPS24系にも別変種が複数あり不統一 |
| 56 | ランレングス圧縮 | `_Strings.py` に3変種 |
| 53 | Dijkstra | あり(2実装) |
| 52 | 遅延セグ木 | `_Lazy_Segment_Tree.py` |
| ~50 | SortedSet/SortedMultiset | `_Sorted_Set.py`(tatyam旧版) |
| 30 | cmb(小さいComb) | Combと統一すべき |
| 29 | MaxFlow/MCF | `_Graph_Algorithm.py` |
| 15 | トポロジカルソート | `_Graph_Algorithm.py` |
| **14** | **行列積・行列累乗** | **ライブラリなし(毎回手書き)** |
| 12 | z-algorithm | `_Strings.py` 内にあるが手書きされ続けている |
| 12 | SCC | `_SCC.py` |
| 10 | ダブリング | `_test.py` に埋没 |
| 9 | LCA | `_Data_Structure.py` の LCATree |
| 8 | CRT | `_ACL_math.py` |
| 該当なし | **2次元累積和 / 2D imos** | **ライブラリなし**(例: `ABC465F.py` で6次元imosを手書き) |
| 該当なし | **グリッドBFS用定数・ユーティリティ**(DIJ, in_grid 等) | 一部 `_test.py`、ほぼ毎回手書き |
| 該当なし | **答えの二分探索(ok/ng)テンプレ** | なし |
| 該当なし | **ワーシャルフロイド** | なし |

## 2. 目標ファイル構成

再編後、ルートに以下を置く。既存 `_*.py` は**削除せず** `_old/` ディレクトリへ移動(git履歴も残る)。

| 新ファイル | 収録内容 | 主な集約元 |
|---|---|---|
| `lib_dsu.py` | UnionFind(反復・サイズ付き), WeightedUnionFind | `_union_find_tree.py`, `_Data_Structure.py` |
| `lib_segtree.py` | SegTree(汎用+min/max/add特化版), LazySegTree, SegmentTreeBeats, BIT, 転倒数 | `_Data_Structure.py`, `_Lazy_Segment_Tree.py`, `_inversion_num.py` |
| `lib_graph.py` | adjlist系, BFS/01-BFS, Dijkstra(1本化), BellmanFord, ワーシャルフロイド(新規), topological_sort, diameter, LCA, EulerTour, SCC, two_sat, LowLink, Rerooting, Dinic, MCFGraph, 巡回セールスマン | `_Graph_Algorithm.py`, `_SCC.py`, `_Low_Link.py`, `_Rerooting.py`, `_ACL_two_sat.py`, `_test.py` |
| `lib_math.py` | Comb(1本化), ModInt, Eratosthenes(SPF対応), prime_factorize(1本化), divisors, modinv/crt/floor_sum, ext_gcd, 行列積・行列累乗(新規), 基数変換, zeta/mobius | `_Fractions.py`, `_ACL_math.py` |
| `lib_string.py` | RLE(3変種→1本化+文字列版), z_algorithm, KMP, RollingHash, Manacher, edit_distance | `_Strings.py` |
| `lib_fps.py` | NTT/畳み込み, FPS, bostan_mori, sparse系 | `FPS24*.py` の最新実装を正とし `_Convolution.py`, `_FFT_comvolve.py` と突き合わせ |
| `lib_sorted.py` | SortedSet, SortedMultiset(tatyam最新版へ更新), BinaryTrie | `_Sorted_Set.py`, `_Binary_Trie.py` |
| `lib_range.py` | Mo, WaveletMatrix, ConvexHullTrick, BitSet | `_Mo.py`, `_WaveletMatrix.py`, `_Convex_Hull_Trick.py`, `_BitSet.py` |
| `lib_geometry.py` | 幾何統合版 | `_Geometry_GPT.py` を軸に `_Geometry.py` の不足分を取り込み |
| `lib_grid.py`(新規) | DIJ/DXY定数, in_grid, i2hw/hw2i, グリッドBFS, 2次元累積和, 2D imos, グリッド回転/転置 | `_test.py` + 新規 |
| `lib_misc.py` | compress(1本化), Doubling, Knapsack, 答えの二分探索テンプレ, KindDeque, GetMax_and_Delete | `_test.py`, `_GetMax_and_Delete.py` |
| `tools/` | `_make_contest_files.py`, `_folder_move.py`, `_explain.py`, テンプレ2種 | 移動のみ |
| `_old/` | `_AVL_Tree.py`, `_Balancing_Tree.py`, `_Cpp_Set.py`(冒頭に「CPython専用・ジャッジのPyPyでは使用不可」と追記), その他移行済み元ファイル全部 | 削除禁止 |

## 3. フェーズ別作業手順

### Phase 0: 準備
1. 作業ブランチを切る(`git checkout -b library-refactor`)。
2. `_old/`, `tools/` を作成。
3. この指示書の頻度表・重複表と実ファイルを突き合わせ、相違があれば作業前に報告する。

### Phase 1: 再編(挙動を変えない移植)
1. §2 のマッピング通りにコードを移す。**このフェーズではロジック改変禁止**(rename と docstring 追加のみ可)。
2. 重複はこの基準で1本を選ぶ: (a) `LibraryChecker/` や `FPS24*` で verify 済みの実装 > (b) 新しい日付の実装 > (c) 行数が短い実装。落とした変種は `_old/` に残るので消えない。
3. 各公開クラス/関数に docstring を付ける: 1行要約、計算量、引数(0-indexed か 1-indexed か明記)、使用例1つ、依存(併せて貼る必要のあるブロック)。
4. ファイル内はコメント罫線(`# ===== UnionFind =====` 形式)でブロックを区切り、貼り付け単位を明確にする。
5. 各ファイル末尾に `def main(): ...` + サンプル使用コードを置く(既存ライブラリの慣習を踏襲)。

### Phase 2: Library Checker による verify 整備
1. `LibraryChecker/` に不足分の verify スクリプトを追加する。命名は既存に合わせ `LC_<問題名>.py`。対応表(最低限):
   - lib_dsu: Unionfind(既存 `LC_Unionfind.py` を新実装で置き換え確認)
   - lib_segtree: Static Range Sum / Point Add Range Sum(既存あり)/ Range Affine Range Sum(既存あり)/ Static RMQ(既存あり)
   - lib_graph: Shortest Path / SCC / 2 SAT / LCA / Cycle Detection
   - lib_math: Binomial Coefficient (Prime Mod) / Enumerate Primes / Factorize(既存 `LC_factorize.py`)/ Matrix Product(既存 `matrix_product.py`)
   - lib_string: Z Algorithm / Run Enumerate は任意
   - lib_fps: Convolution / Inv of FPS(既存あり)
   - lib_sorted: Predecessor Problem(既存あり)
2. 各 verify スクリプトの冒頭コメントに問題URLを書く。
3. ローカル確認用に `tests/` を作り、verify に対応する小さいランダムテスト(愚直解との突き合わせ、pytest 不要の単純 assert スクリプトで可)を置く。
4. Library Checker への提出は人間が行うので、**提出前提の完成形(標準入出力・PyPy想定)**にしておくこと。

### Phase 3: 未ライブラリ化パターンの新規実装(頻度順)
1. `lib_grid.py`: DIJ/DXY 定数、in_grid、グリッドBFS(距離配列返却)、2次元累積和クラス(構築 O(HW)・矩形和 O(1))、2D imos。
2. `lib_math.py` に行列積・行列累乗(mod引数付き、リストのリスト実装)。verify: Matrix Product。
3. `lib_misc.py` に答えの二分探索テンプレ(`ok/ng` 形式、整数版・実数版)。
4. `lib_graph.py` にワーシャルフロイド、`adjlist` 統一版(directed/undirected, 0/1-indexed を引数で指定)。
5. RLE を1本化(list版・文字列版の2関数のみ)。
6. Comb を1本化: 既存 `class Comb`(階乗前計算)を正とし、`cmb`(その場計算)と HugeComb(n が大きく r が小さい場合)を同ブロックに併記。

### Phase 4: PyPy 向け速度改善(要ベンチ)
このフェーズのみロジック変更可。**各項目とも変更前後を PyPy でベンチし、結果を表で報告すること**(ベンチスクリプトは `benchmarks/` に保存。想定規模: N=2×10^5、クエリ2×10^5)。

1. **UnionFind**: `_union_find_tree.py` 版は `members`(defaultdict of set)と `roots` を全 unite で常時更新しており、これが不要な問題では純粋なオーバーヘッド。統合版は「軽量版(par 配列のみ、find は反復 path-halving)」を標準とし、members が必要なときの取得メソッド(O(N) で構築)を別途用意する。再帰 find は PyPy では関数呼び出しが積み重なると遅く、RecursionError リスクもあるため反復に統一。
2. **SegTree**: 単位元 `float("inf")` の使用をやめ int を推奨(PyPy は int/float 混在で unboxing が阻害される)。汎用版(segfunc 引数)に加えて min/max/add 特化版(演算インライン)を用意し、ベンチで差を記録。
3. **SortedSet/SortedMultiset**: tatyam 版最新(GitHub の SortedSet リポジトリ)と現行を突き合わせ、差分があれば更新して Predecessor Problem でベンチ。
4. **NTT/FPS**: `FPS24*.py` 内の実装と `_Convolution.py` の FFT class を Convolution 問題でベンチ比較し、速い方を `lib_fps.py` の正とする。
5. **再帰実装の反復化**: EulerTour, LowLink, Rerooting, SCC 周りに再帰があれば反復化(N=2×10^5 の直線グラフで RecursionError にならないことをテストに含める)。
6. **規約として明記**(各ファイル冒頭コメント): `lru_cache` 禁止(PyPyで遅い)、再帰DFS原則禁止、文字列連結は join、`10**18` を INF とする(float inf 不使用)。
7. **一括入力テンプレ**: `sys.stdin.buffer.read().split()` 方式の高速入力テンプレを `lib_misc.py` に追加(現行 readline 方式はテンプレとして維持、大入力問題用の代替として)。

### Phase 5: 仕上げ
1. `_LIBRARY_INDEX.md` を作成: 機能 → ファイル → クラス/関数名 → 計算量 → verify 問題URL の一覧表。「どこに何があるか」を1枚で引けるようにする(埋没の再発防止が目的)。
2. `README.md` にライブラリ運用ルール(貼り付け方式、規約、ベンチ方法)を追記。

## 4. 受け入れ基準

- [ ] コンテスト解答ファイル(`ABC*.py` 等)への変更が git diff 上ゼロであること
- [ ] 旧 `_*.py` が `_old/` に全て残っていること(削除ゼロ)
- [ ] `LibraryChecker/` の全 verify スクリプトがローカルのサンプル入力で正答すること(提出用に完成していること)
- [ ] `tests/` のランダムテストが全て通ること
- [ ] Phase 4 の各項目にベンチ結果(before/after、PyPy)が添付されていること
- [ ] 全公開クラス/関数に docstring(計算量含む)があること
- [ ] `_LIBRARY_INDEX.md` が実ファイルと一致していること

## 5. Codex への注意事項

- Phase 1 では「良かれと思った改良」をしない。移植と改変のフェーズを混ぜると verify で切り分けできなくなる。
- 貼り付け運用が前提。モジュール間 import を導入しない。
- 実装の正が複数あって迷ったら、`LibraryChecker/` と `FPS24*.py` にある実装(verify 済み・最新)を優先する。
- 幾何(`_Geometry_GPT.py`)と SegmentTreeBeats は verify 問題が限られるため、移植+ランダムテストのみで可。
- `_Cpp_Set.py` と `set_wrapper.cpp` / `setup.py` は CPython 専用の実験。手を入れず `_old/` へ。
- 作業単位ごとにコミットを分ける(Phase 1 のファイル統合1本 = 1コミット目安)。
