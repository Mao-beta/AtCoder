"""コンテスト解答を整理する。確認のみが既定で、--apply を付けると移動する。"""

import argparse
from collections import Counter
from pathlib import Path
import re


ARCHIVE = re.compile(r"ABC|ARC|AGC|ADT|PAST\d{0,3}|yuki|EDPC|tenkei90")


def destination_for(root, source):
    """既知の命名規則だけを扱い、別解を表す接尾辞は保持する。"""
    name = source.name
    if match := re.fullmatch(r"(ABC|ARC|AGC)(\d{3})([A-Z].*)\.py", name):
        kind, number, _ = match.groups()
        return root / kind / f"{kind}{number}" / name
    if match := re.fullmatch(r"PAST(\d{1,3})([A-Z].*)\.py", name):
        number, problem = match.groups()
        contest = f"PAST{int(number):03d}"
        return root / "PAST" / contest / f"{contest}{problem}.py"
    if match := re.fullmatch(r"ADT_(\d{8})_([1-3][A-Z].*)\.py", name):
        return root / "ADT" / match[1] / name
    if match := re.fullmatch(r"yuki_(\d+).*\.(?:py|txt)", name):
        return root / "yuki" / f"{int(match[1]) // 100:02d}xx" / name
    if re.fullmatch(r"EDPC[_A-Z].*\.py", name):
        return root / "EDPC" / name
    if re.fullmatch(r"tenkei90[_\d].*\.py", name):
        return root / "tenkei90" / name
    return None


def plan_moves(root, include_root=True):
    """対象フォルダだけを走査し、上書きしない移動先を確定する。"""
    root = root.resolve()
    sources = list(root.glob("*")) if include_root else []
    for directory in sorted(root.iterdir()):
        if directory.is_dir() and ARCHIVE.fullmatch(directory.name):
            sources.extend(directory.rglob("*"))
    moves = []
    reserved = set()
    for source in sorted(sources, key=lambda p: (len(p.parts), str(p))):
        if not source.is_file() or source.is_symlink():
            continue
        target = destination_for(root, source)
        if target is None or target == source:
            continue
        source.resolve().relative_to(root)
        target.resolve().relative_to(root)
        original = target
        alternative = 2
        while target.exists() or target in reserved:
            target = original.with_name(f"{original.stem}_alt{alternative}{original.suffix}")
            alternative += 1
        reserved.add(target)
        moves.append((source, target))
    return moves


def apply_moves(root, moves):
    """既存ファイルを保護して移動し、移動元の空フォルダだけを取り除く。"""
    root = root.resolve()
    for source, target in moves:
        source.resolve().relative_to(root)
        target.resolve().relative_to(root)
        if not source.is_file():
            raise FileNotFoundError(source)
        if target.exists():
            raise FileExistsError(target)
    for source, target in moves:
        target.parent.mkdir(parents=True, exist_ok=True)
        # Windowsのrenameは既存の移動先を上書きせず、エラーにする。
        source.rename(target)
    for source, _ in moves:
        parent = source.parent
        while parent != root:
            try:
                parent.rmdir()
            except OSError:
                break
            parent = parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="プレビューした規則で実際に移動する")
    parser.add_argument("--archives-only", action="store_true", help="直下の作業中ファイルを残し、既存の保存先だけを整理する")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    moves = plan_moves(root, include_root=not args.archives_only)
    for source, target in moves[:20]:
        print(f"{source.relative_to(root)} -> {target.relative_to(root)}")
    if len(moves) > 20:
        print(f"... ほか {len(moves) - 20} ファイル")
    counts = Counter(target.relative_to(root).parts[0] for _, target in moves)
    summary = ', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))
    print(f"対象: {len(moves)} ファイル" + (f" ({summary})" if summary else ""))
    if args.apply:
        apply_moves(root, moves)
        print("移動完了")
    elif moves:
        print("変更していません。実行するには --apply を付けてください。")


if __name__ == "__main__":
    main()
