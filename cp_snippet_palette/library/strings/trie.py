"""Trie・Aho–Corasick。出典: ABC362G, yuki_0430を配列と辞書で整理。
PyPy向け。Ahoは検索ごとの計数をfail木で集約し、出力リストの複製を避ける。
"""

from collections import deque


class Trie:
    def __init__(self):
        self.next = [{}]
        self.counts = [0]
        self.terminals = [0]

    def add(self, word):
        """O(|word|)。重複と空文字列に対応。"""
        u = 0
        self.counts[u] += 1
        for ch in word:
            if ch not in self.next[u]:
                self.next[u][ch] = len(self.next)
                self.next.append({})
                self.counts.append(0)
                self.terminals.append(0)
            u = self.next[u][ch]
            self.counts[u] += 1
        self.terminals[u] += 1

    def _node(self, word):
        u = 0
        for ch in word:
            u = self.next[u].get(ch, -1)
            if u == -1:
                break
        return u

    def count(self, word):
        u = self._node(word)
        return self.terminals[u] if u >= 0 else 0

    def count_prefix(self, prefix):
        u = self._node(prefix)
        return self.counts[u] if u >= 0 else 0


class AhoCorasick:
    def __init__(self, patterns):
        self.next = [{}]
        self.fail = [0]
        self.ends = []
        for word in patterns:
            u = 0
            for ch in word:
                if ch not in self.next[u]:
                    self.next[u][ch] = len(self.next)
                    self.next.append({})
                    self.fail.append(0)
                u = self.next[u][ch]
            self.ends.append(u)
        queue = deque(self.next[0].values())
        self.order = []
        while queue:
            u = queue.popleft()
            self.order.append(u)
            for ch, v in self.next[u].items():
                f = self.fail[u]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[v] = self.next[f].get(ch, 0)
                queue.append(v)

    def count(self, text):
        """パターンごとの出現数。重複一致を含む。O(|text|+ノード数)。"""
        visits = [0] * len(self.next)
        u = 0
        for ch in text:
            while u and ch not in self.next[u]:
                u = self.fail[u]
            u = self.next[u].get(ch, 0)
            visits[u] += 1
        for v in reversed(self.order):
            visits[self.fail[v]] += visits[v]
        visits[0] = len(text) + 1
        return [visits[v] for v in self.ends]
