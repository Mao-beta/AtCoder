# Library Checkerへの対応

2026-10-17、第1弾。AtCoder青以上で使う機会が多い区間処理・グラフ分解・割当・線形代数を優先して追加した。色と用途の対応は優先順位を決めるための目安で、問題の公式難度区分ではない。

[公式の問題一覧](https://github.com/yosupo06/library-checker-problems/blob/master/categories.toml)は確認時点で235問題。以下の10問題は、今回ライブラリの実装・拡張から提出形式の入出力まで用意したもの。既存ライブラリのverify候補一覧は[VERIFY_PROBLEMS.md](../VERIFY_PROBLEMS.md)にある。候補の掲載と、提出用コードを用意して検査した状態は区別する。

## 今回対応した問題

| 問題 | 使用するAPI | 主な用途・条件 |
|---|---|---|
| [Queue Operate All Composite](https://judge.yosupo.jp/problem/queue_operate_all_composite) | [AggregateQueue(op,e)](../library/structures/aggregate_queue.py) | SWAG。非可換な関数合成を含む、キュー全体の集約。追加・先頭削除は償却O(1)回のop。 |
| [Segment Add Get Min](https://judge.yosupo.jp/problem/segment_add_get_min) | [LiChaoTree(xs).add_segment(l,r,a,b)](../library/structures/li_chao.py) | 区間内だけ有効な直線、最小化DP。座標は事前登録、区間は[l,r)。追加O(log²n)、問い合わせO(log n)。 |
| [Biconnected Components](https://judge.yosupo.jp/problem/biconnected_components) | [LowLink.biconnected_components / block_cut_tree](../library/graphs/lowlink.py) | 関節点をまたぐ経路・連結性の問題。孤立点・多重辺対応、非再帰O(V+E)。 |
| [Assignment Problem](https://judge.yosupo.jp/problem/assignment) | [assignment(cost)](../library/graphs/assignment.py) | Hungarian法。負費用可、行数n≤列数m、O(n²m)。最適費用と割当先を返す。 |
| [Determinant of Matrix](https://judge.yosupo.jp/problem/matrix_det) | [matrix_det(a,mod)](../library/math/linear_algebra.py) | 素数mod上の行列式、O(n³)。合成数modには対応しない。 |
| [Rank of Matrix](https://judge.yosupo.jp/problem/matrix_rank) | [matrix_rank(a,mod)](../library/math/linear_algebra.py) | 矩形行列・0行/0列対応。O(nm min(n,m))。 |
| [Inverse Matrix](https://judge.yosupo.jp/problem/inverse_matrix) | [inverse_matrix(a,mod)](../library/math/linear_algebra.py) | 逆行列。特異ならNone。O(n³)。 |
| [System of Linear Equations](https://judge.yosupo.jp/problem/system_of_linear_equations) | [linear_equations(a,b,mod)](../library/math/linear_algebra.py) | 特解と同次解の基底を返す。解なしNone。自由変数・不定系も扱う。 |
| [System of Linear Equations (Mod 2)](https://judge.yosupo.jp/problem/system_of_linear_equations_mod_2) | [linear_equations_gf2(rows,rhs,variables)](../library/math/bit_transforms.py) | XOR制約。行・解・基底を整数bitsetで表す。従来のsolve_gf2も保持。 |
| [Bitwise Xor Convolution](https://judge.yosupo.jp/problem/bitwise_xor_convolution) | [xor_convolution(a,b,mod)](../library/math/bit_transforms.py) | XORで添字を合成する数え上げ。FWHT、O(n log n)。同じ長さ2^k、奇数mod。 |

## 提出用の1ファイルを作る

リポジトリ直下で実行する。検索パレットからは今までどおり、必要なライブラリだけをコピーできる。

```powershell
Set-Location D:\Kyopro\AtCoder
# 対応している問題ID
.\.venv\Scripts\python.exe cp_snippet_palette\verify\build.py --list
# ライブラリと入出力をまとめる
.\.venv\Scripts\python.exe cp_snippet_palette\verify\build.py segment_add_get_min
```

生成先は`cp_snippet_palette/verify/build/segment_add_get_min.py`。このファイル全体をLibrary Checkerに提出する。生成物にはローカルライブラリのimportを残さず、標準ライブラリだけで動作する。再生成すると同名の生成物を更新するため、問題固有の入出力を直す場合は`library_checker/`側を編集する。`build/`はGitの対象外。

ローカル実行は次の形式。入力ファイル名は自分のものに置き換える。

```powershell
Get-Content .\input.txt | & D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\verify\build\segment_add_get_min.py
```

アダプター自体も、リポジトリ直下から`python -m cp_snippet_palette.verify.library_checker.segment_add_get_min`の形式で実行できる。提出にはbuildでまとめたファイルを使う。

## 確認済みの範囲

- Windows版PyPy 7.3.23 / Python 3.11.15で既存34テストと追加7テストが成功。
- 追加テスト内で公式サンプル入力23件を使用し、生成した10種類の提出コードを独立したプロセスで実行した。出力は愚直実装や数式で検査し、非一意解は最適値・方程式・基底の独立性を確認した。
- 最大制約に相当する代表入力でも生成済みコードを実行した。割当500×500、逆行列500×500、XOR畳み込み2^20要素、GF(2)方程式4096×4096、二重連結成分50万頂点のパス、区間直線N=Q=20万。それぞれ既知の答え、または主要な数学的条件で出力を確認した。
- 公式ジェネレーターの全テスト実行・オンライン提出・AC判定は未実施。上の代表入力の成功は、すべての最悪ケースでの時間・メモリ制限を保証しない。Codonのコンパイル確認も未実施。特にGF(2)の大きな整数bitsetはPyPy向け。

```powershell
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\tests\test_library.py -v
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\tests\test_library_checker.py -v
```

サンプル入力の出典・リビジョンは[samples/README.md](samples/README.md)に記載。

## 次の追加候補

青以上を目安に、必要なアルゴリズム・復元・入出力が不足しているものから進める。以下を次の追加候補として記録した。

1. **オフライン・永続化**：Rollback DSU、動的連結性、Persistent Unionfind、Deque Operate All Composite。
2. **多項式・畳み込み**：多点評価、Taylor Shift、多項式除算、Subset Convolution、別の法での畳み込み。既存FPSで利用できる機能は再利用する。
3. **グラフ・木**：有向最小全域木、最小費用b-flow、木の距離頻度。計算量とPyPyの実測を見て優先順位を調整する。
4. **出力の不足**：最近点対の点ID復元、Steiner木の辺復元、GF(2)の逆行列。既存の「値だけ返す」APIは互換性を保って拡張する。
