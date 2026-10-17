# 公式サンプル入力の出典

このフォルダの23個の`.in`は、[Library Checker公式problemリポジトリ](https://github.com/yosupo06/library-checker-problems)の`gen/example_*.in`を変更せず保存したもの。

- リビジョン：`1814c4e5205517e368bb57a8d1127eb961cfeaae`
- 取得日：2026-10-17
- ライセンス：[Apache License 2.0](LICENSE)。リポジトリのLICENSEを同梱。
- Data Structure：`queue_operate_all_composite`、`segment_add_get_min`
- Graph：`biconnected_components`、`assignment`
- Linear Algebra：`matrix_det`、`matrix_rank`、`inverse_matrix`、`system_of_linear_equations`、`system_of_linear_equations_mod_2`
- Convolution：`bitwise_xor_convolution`

サンプル出力の文字列を同梱したものではない。`tests/test_library_checker.py`が入力から独立した愚直解や数式を用いて検査する。線形方程式の基底、割当、成分の順序には複数の正解があるため、条件を満たすかを確認する。
