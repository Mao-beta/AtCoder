"""Library Checker/AtCoder用のアダプターとライブラリを、提出可能な1ファイルにまとめる。"""

import argparse
import ast
from pathlib import Path

ROOT = Path(__file__).absolute().parent
PALETTE = ROOT.parent
PREFIX = "cp_snippet_palette."


def problems(atcoder=False):
    folder = "atcoder" if atcoder else "library_checker"
    return sorted(path.stem for path in (ROOT / folder).glob("*.py"))


def bundle(problem, atcoder=False):
    if problem not in problems(atcoder):
        raise ValueError("unknown problem: " + problem)
    folder = "atcoder" if atcoder else "library_checker"
    driver = (ROOT / folder / (problem + ".py")).read_text(encoding="utf8")
    modules, remove = [], set()
    for node in ast.parse(driver).body:
        if (
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith(PREFIX)
        ):
            if any(alias.asname or alias.name == "*" for alias in node.names):
                raise ValueError(
                    "only explicit unaliased library imports are supported"
                )
            path = PALETTE / (node.module[len(PREFIX) :].replace(".", "/") + ".py")
            if path not in modules:
                modules.append(path)
            remove.update(range(node.lineno, node.end_lineno + 1))
    pieces = [driver.splitlines()[0]]
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
    parser.add_argument("problem", nargs="?")
    parser.add_argument(
        "--atcoder", action="store_true", help="AtCoderのアダプターを使う"
    )
    parser.add_argument("--list", action="store_true", help="対応する問題IDを表示")
    args = parser.parse_args()
    if args.list:
        print("\n".join(problems(args.atcoder)))
    if args.problem:
        if args.problem not in problems(args.atcoder):
            parser.error(
                "対象の問題IDを--listで確認してください。AtCoderは--atcoderを付けます。"
            )
        source = bundle(args.problem, args.atcoder)
        target = ROOT / "build" / (args.problem + ".py")
        target.parent.mkdir(exist_ok=True)
        target.write_text(source, encoding="utf8")
        print(target)
    elif not args.list:
        parser.print_help()


if __name__ == "__main__":
    main()
