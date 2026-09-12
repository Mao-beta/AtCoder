# AtCoder Python環境

確認日: 2026-09-12

- プロジェクト: `D:\Kyopro\AtCoder`
- 仮想環境: `D:\Kyopro\AtCoder\.venv`
- PyCharmのインタープリター: `D:\Kyopro\AtCoder\.venv\Scripts\python.exe`
- Python: CPython 3.13.7、環境・パッケージ管理: uv
- Python本体: `D:\Kyopro\.python\cpython-3.13.7\python.exe`

PyCharmでの起動時にAppData配下のPython本体が見つからないエラーが出たため、Python本体を作業フォルダ内へコピーし、uvで既存の仮想環境の参照先を修復しました。導入済みパッケージは保持しています。`.python` ディレクトリは仮想環境の実行に必要です。

PyCharmでは `D:\Kyopro\AtCoder\.venv\Scripts\python.exe` を既存のインタープリターとして指定します。以前のエラーが表示されたままの場合は、PyCharmを再起動してから選択し直してください。

[AtCoderの公式CPython環境](https://img.atcoder.jp/file/language-update/2025-10/082-3-13_cpython.toml)に記載された43種類のうち、39種類を導入しました。バージョンは `requirements-atcoder.txt` に固定しています。AC Library Python版も公式環境と同じコミットを使用しています。

NumPy、SciPy、Numba、pandas、Polars、SymPy、NetworkX、sortedcontainers、AC Library Python版、PuLP、OR-Tools、Z3、scikit-learn、LightGBM、CPU版PyTorchなどを使用できます。

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

導入済みライブラリのバージョン、主要38種類のimport、NumbaのJITコンパイル、PyTorchのCPU計算、AC LibraryのDSU、sortedcontainers、PuLP/CBC、OR-Tools/CP-SATの動作を確認しました。

参照先の修復後に、全41パッケージ（AtCoderの39種類とpip・setuptools）のバージョンが変わっていないこと、主要38種類のimport、Numba・PyTorch・DSUの動作、`uv pip check`の成功を確認しました。PyCharm同梱のJavaランタイムから実行したスレッド処理モデルの判定コマンドも、終了コード0・出力`True`でした。PyCharmの画面操作は行っていません。

AtCoderはLinux環境のため、Windows上のこの環境とOSや実行速度は異なります。Numbaは同じバージョンのWindows用配布物を使用しており、AtCoder独自のCUDA機能除去パッチは適用していません。
