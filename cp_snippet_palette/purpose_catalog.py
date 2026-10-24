"""LIBRARY_GUIDE.mdの逆引き表と分類コメントをGUI用に読み取る。"""

from dataclasses import dataclass
from pathlib import Path
import re

import cp_palette as core


@dataclass(frozen=True)
class Purpose:
    path: tuple[str, ...]
    goal: str
    api: str
    target: str
    condition: str
    keywords: str

    def matches(self, query):
        """空白区切りの全語を、目的・条件・API・分類から検索する。"""
        text = core.norm(" ".join((*self.path, self.goal, self.api,
                                   self.condition, self.keywords)))
        return all(word in text for word in core.norm(query).split())


def load_purposes(path=None):
    """文書を読むだけで、リンク先のコードは実行しない。"""
    source = Path(path) if path else core.ROOT / "LIBRARY_GUIDE.md"
    content = source.read_text(encoding="utf-8")
    section = content.split("## 目的から探す逆引き\n", 1)[1].split("\n## ", 1)[0]
    result = []
    heading, route = "その他", ()
    for line in section.splitlines():
        match = re.search(r"<!-- navigator: (.+?) -->", line)
        route = tuple(part.strip() for part in match[1].split(" > ")) if match else ()
        line = re.sub(r"<!-- navigator: .+? -->\s*", "", line)
        if line.startswith("### "):
            heading = line[4:].strip()
        elif line.startswith("|") and "](" in line:
            cells = [cell.strip() for cell in line.strip("| ").split("|")]
            if len(cells) != 4:
                raise ValueError(f"逆引き表の列数が不正です: {line}")
            for api, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", cells[1]):
                file = (core.ROOT / target).resolve()
                if file.suffix != ".py" or not file.is_relative_to(core.ROOT):
                    raise ValueError(f"逆引きのリンク先が不正です: {target}")
                result.append(Purpose(route or ("その他", heading), cells[0], api,
                                      target, cells[2], cells[3].strip("`")))
            # 分類は各行に付ける。追加した未分類行も「その他」へ表示する。
    return result
