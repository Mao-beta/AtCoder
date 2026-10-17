# AtCoder Python環境

環境構築・動作確認: 2026-09-12。実行ファイル・パッケージメタデータの再確認: 2026-10-17。

- プロジェクト: `D:\Kyopro\AtCoder`
- 仮想環境: `D:\Kyopro\AtCoder\.venv`
- PyCharmのインタープリター: `D:\Kyopro\AtCoder\.venv\Scripts\python.exe`
- Python: CPython 3.13.7、環境・パッケージ管理: uv
- Python本体: `D:\Kyopro\.python\cpython-3.13.7\python.exe`

PyCharmでの起動時にAppData配下のPython本体が見つからないエラーが出たため、Python本体を作業フォルダ内へコピーし、uvで既存の仮想環境の参照先を修復しました。導入済みパッケージは保持しています。`.python` ディレクトリは仮想環境の実行に必要です。

PyCharmでは `D:\Kyopro\AtCoder\.venv\Scripts\python.exe` を既存のインタープリターとして指定します。以前のエラーが表示されたままの場合は、PyCharmを再起動してから選択し直してください。

導入時に参照した[AtCoderの公式CPython環境](https://img.atcoder.jp/file/language-update/2025-10/082-3-13_cpython.toml)に記載された43種類のうち、39種類を導入しました。バージョンは `requirements-atcoder.txt` に固定しています。AC Library Python版も参照元と同じコミットを使用しています。2026-10-17に39種類のバージョンまたは配布元URLがこのファイルと一致することを再確認しました。AtCoder側の全言語環境を継続同期する設定ではありません。

NumPy、SciPy、Numba、pandas、Polars、SymPy、NetworkX、sortedcontainers、AC Library Python版、PuLP、OR-Tools、Z3、scikit-learn、LightGBM、CPU版PyTorchなどを使用できます。

## 提出用ライブラリの検証環境

uvで別途用意したPyPyは`D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe`。2026-10-17にPython 3.11.15 / PyPy 7.3.23の起動を確認しました。上記CPython仮想環境とは別環境で、39種類のパッケージをPyPyにも導入したという意味ではありません。

検索ツールはCPython仮想環境の`pythonw.exe`で起動し、提出用ライブラリはPyPyでも検証しています。対象と検証結果は[LIBRARY_GUIDE.md](cp_snippet_palette/LIBRARY_GUIDE.md)、検索ツールの操作は[LOCAL_USAGE.md](cp_snippet_palette/LOCAL_USAGE.md)を参照してください。Codonのコンパイル確認は未実施です。

## 未導入のライブラリ

次の4種類はソースからのビルドにMSVCとWindows SDKが必要です。Microsoft Build Toolsの導入時のWindows管理者確認がキャンセルされたため、未導入です。

- `acl-cpp-python==0.6.2`（`acl_cpp`）
- `cppyy==3.5.0`
- `cppyy-backend==1.15.3`
- `CPyCppyy==1.13.0`

`cppyy-cling==6.32.8`は導入済みですが、上記の関連パッケージが揃うまでは`import cppyy`は利用できません。

## 導入済みパッケージの再インストール

プロジェクトのディレクトリで実行します。

```powershell
uv pip install --python .venv\Scripts\python.exe --link-mode copy -r requirements-atcoder.txt
uv pip check --python .venv\Scripts\python.exe
```

## 確認した動作

以下のimport・計算・依存関係検査は環境構築と修復時の記録です。2026-10-17の文書照合では全importを再実行せず、実行環境とパッケージメタデータを確認しました。

導入済みライブラリのバージョン、主要38種類のimport、NumbaのJITコンパイル、PyTorchのCPU計算、AC LibraryのDSU、sortedcontainers、PuLP/CBC、OR-Tools/CP-SATの動作を確認しました。

参照先の修復後に、全41パッケージ（AtCoderの39種類とpip・setuptools）のバージョンが変わっていないこと、主要38種類のimport、Numba・PyTorch・DSUの動作、`uv pip check`の成功を確認しました。PyCharm同梱のJavaランタイムから実行したスレッド処理モデルの判定コマンドも、終了コード0・出力`True`でした。PyCharmの画面操作は行っていません。

AtCoderはLinux環境のため、Windows上のこの環境とOSや実行速度は異なります。Numbaは同じバージョンのWindows用配布物を使用しており、AtCoder独自のCUDA機能除去パッチは適用していません。
