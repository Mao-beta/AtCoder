"""Library Checker用のアダプターとライブラリを、提出可能な1ファイルにまとめる。"""

import argparse
import ast
from pathlib import Path

ROOT = Path(__file__).absolute().parent
PALETTE = ROOT.parent
PREFIX = "cp_snippet_palette.library."


def problems():
    return sorted(path.stem for path in (ROOT / "library_checker").glob("*.py"))


def bundle(problem):
    if problem not in problems():
        raise ValueError("unknown problem: " + problem)
    driver = (ROOT / "library_checker" / (problem + ".py")).read_text(encoding="utf8")
    modules, remove = [], set()
    for node in ast.parse(driver).body:
        if isinstance(node, ast.ImportFrom) and node.module.startswith(PREFIX):
            if any(alias.asname or alias.name == "*" for alias in node.names):
                raise ValueError(
                    "only explicit unaliased library imports are supported"
                )
            path = (
                PALETTE
                / "library"
                / (node.module[len(PREFIX) :].replace(".", "/") + ".py")
            )
            if path not in modules:
                modules.append(path)
            remove.update(range(node.lineno, node.end_lineno + 1))
    pieces = [
        f"# verification-helper: PROBLEM https://judge.yosupo.jp/problem/{problem}"
    ]
    for path in modules:
        pieces.append(
            f"# Source: {path.relative_to(PALETTE).as_posix()}\n"
            + path.read_text(encoding="utf8")
        )
    pieces.append(
        "\n".join(
            line for i, line in enumerate(driver.splitlines(), 1) if i not in remove
        )
    )
    source = "\n\n".join(pieces) + "\n"
    compile(source, problem + ".py", "exec")
    return source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem", nargs="?", choices=problems())
    parser.add_argument("--list", action="store_true", help="対応する問題IDを表示")
    args = parser.parse_args()
    if args.list:
        print("\n".join(problems()))
    if args.problem:
        source = bundle(args.problem)
        target = ROOT / "build" / (args.problem + ".py")
        target.parent.mkdir(exist_ok=True)
        target.write_text(source, encoding="utf8")
        print(target)
    elif not args.list:
        parser.print_help()


if __name__ == "__main__":
    main()
