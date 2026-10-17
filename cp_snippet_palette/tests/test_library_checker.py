"""追加したLC向けAPIと、1ファイル化した提出コードの公式サンプル入力を確認する。
出力が一意でない問題は文字列一致ではなく、最適値・方程式・基底を検査する。
"""

from collections import deque
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import random
import runpy
import subprocess
import sys
import unittest

ROOT = Path(__file__).absolute().parents[1]
MOD = 998244353


@lru_cache(None)
def lib(name):
    return runpy.run_path(str(ROOT / "library" / (name + ".py")))


def determinant_naive(a, mod):
    total = 0
    for p in permutations(range(len(a))):
        term = (-1) ** sum(
            p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))
        )
        for i, j in enumerate(p):
            term *= a[i][j]
        total += term
    return total % mod


def rank_naive(a, mod):
    n, m = len(a), len(a[0]) if a else 0
    for size in range(min(n, m), 0, -1):
        for rows in combinations(range(n), size):
            for cols in combinations(range(m), size):
                if determinant_naive([[a[i][j] for j in cols] for i in rows], mod):
                    return size
    return 0


def bcc_naive(n, edges):
    graph = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            graph[u].add(v)
            graph[v].add(u)

    def connected(vertices):
        if not vertices:
            return True
        visited = {next(iter(vertices))}
        queue = list(visited)
        for u in queue:
            for v in graph[u] & vertices - visited:
                visited.add(v)
                queue.append(v)
        return visited == vertices

    candidates = []
    for size in range(n, 0, -1):
        for items in combinations(range(n), size):
            vertices = frozenset(items)
            if any(vertices <= old for old in candidates):
                continue
            if connected(vertices) and all(connected(vertices - {v}) for v in vertices):
                candidates.append(vertices)
    return set(candidates)


class LibraryCheckerTests(unittest.TestCase):
    def test_aggregate_queue(self):
        Queue = lib("structures/aggregate_queue")["AggregateQueue"]
        queue, reference = Queue(lambda x, y: x + y, ""), deque()
        rng = random.Random(100)
        for _ in range(80):
            if not reference or rng.randrange(3):
                value = chr(97 + rng.randrange(5))
                queue.append(value)
                reference.append(value)
            else:
                self.assertEqual(queue.popleft(), reference.popleft())
            self.assertEqual(queue.prod(), "".join(reference))
            self.assertEqual(len(queue), len(reference))
        queue.clear()
        self.assertEqual(queue.prod(), "")
        with self.assertRaises(IndexError):
            queue.popleft()

    def test_segment_li_chao(self):
        Tree = lib("structures/li_chao")["LiChaoTree"]
        xs = [-100, -9, -1, 0, 2, 13, 100]
        rng = random.Random(101)
        for mode in ("min", "max"):
            tree = Tree(xs + [0], mode)
            lines = []
            self.assertIsNone(tree.query(0))
            for step in range(30):
                left, right = sorted(rng.sample(range(-110, 111), 2))
                a, b = rng.randrange(-20, 21), rng.randrange(-20, 21)
                if step % 7 == 0:
                    tree.add_line(a, b)
                    lines.append((-1000, 1000, a, b))
                else:
                    tree.add_segment(left, right, a, b)
                    lines.append((left, right, a, b))
                for x in xs:
                    values = [a * x + b for l, r, a, b in lines if l <= x < r]
                    expected = (
                        (min(values) if mode == "min" else max(values))
                        if values
                        else None
                    )
                    self.assertEqual(tree.query(x), expected)
        tree = Tree([0, 1, 2])
        tree.add_segment(0, 1, 0, 10**100)
        self.assertEqual(tree.query(0), 10**100)
        self.assertIsNone(tree.query(1))
        with self.assertRaises(ValueError):
            tree.query(3)
        Tree([]).add_segment(0, 1, 2, 3)

    def test_biconnected_components(self):
        LowLink = lib("graphs/lowlink")["LowLink"]
        rng = random.Random(102)
        examples = [(1, []), (4, [(0, 1), (0, 1), (1, 2)]), (2, [(0, 0)])]
        for _ in range(10):
            edges = [
                (u, v)
                for u in range(6)
                for v in range(u + 1, 6)
                if rng.randrange(3) == 0
            ]
            examples.append((6, edges))
        for n, edges in examples:
            low = LowLink(n, edges)
            self.assertEqual(
                set(map(frozenset, low.biconnected_components())), bcc_naive(n, edges)
            )
            forest = low.block_cut_tree()
            for u, neighbors in enumerate(forest):
                self.assertEqual(len(neighbors), len(set(neighbors)))
                for v in neighbors:
                    self.assertIn(u, forest[v])
            self.assertEqual(len(forest), n + len(low.biconnected_components()))

    def test_assignment(self):
        assign = lib("graphs/assignment")["assignment"]
        rng = random.Random(103)
        self.assertEqual(assign([]), (0, []))
        for n in range(1, 6):
            for m in (n, n + 1):
                a = [[rng.randrange(-8, 9) for _ in range(m)] for _ in range(n)]
                saved = [row[:] for row in a]
                value, result = assign(a)
                best = min(
                    sum(a[i][p[i]] for i in range(n)) for p in permutations(range(m), n)
                )
                self.assertEqual(value, best)
                self.assertEqual(sum(a[i][j] for i, j in enumerate(result)), best)
                self.assertEqual(len(set(result)), n)
                self.assertEqual(a, saved)
        with self.assertRaises(ValueError):
            assign([[1], [2]])

    def test_modular_linear_algebra(self):
        math = lib("math/linear_algebra")
        rng = random.Random(104)
        for n in range(5):
            a = [[rng.randrange(-7, 8) for _ in range(n)] for _ in range(n)]
            saved = [row[:] for row in a]
            det = determinant_naive(a, 7)
            self.assertEqual(math["matrix_det"](a, 7), det)
            self.assertEqual(math["matrix_rank"](a, 7), rank_naive(a, 7))
            inverse = math["inverse_matrix"](a, 7)
            if det == 0:
                self.assertIsNone(inverse)
            else:
                for i in range(n):
                    for j in range(n):
                        self.assertEqual(
                            sum(a[i][k] * inverse[k][j] for k in range(n)) % 7,
                            int(i == j),
                        )
            self.assertEqual(a, saved)
        for n, m in ((0, 3), (2, 3), (4, 3), (2, 0)):
            for _ in range(4):
                a = [[rng.randrange(3) for _ in range(m)] for _ in range(n)]
                b = [rng.randrange(3) for _ in range(n)]
                expected = {
                    x
                    for x in product(range(3), repeat=m)
                    if all(
                        sum(v * w for v, w in zip(row, x)) % 3 == y
                        for row, y in zip(a, b)
                    )
                }
                result = math["linear_equations"](a, b, 3, variables=m)
                if not expected:
                    self.assertIsNone(result)
                else:
                    solution, basis = result
                    span = {
                        tuple(
                            (
                                solution[j]
                                + sum(t[i] * basis[i][j] for i in range(len(basis)))
                            )
                            % 3
                            for j in range(m)
                        )
                        for t in product(range(3), repeat=len(basis))
                    }
                    self.assertEqual(span, expected)
        with self.assertRaises(ValueError):
            math["matrix_det"]([[1, 2]])

    def test_gf2_and_xor_convolution(self):
        math = lib("math/bit_transforms")
        rng = random.Random(105)
        for _ in range(12):
            rows = [rng.randrange(8) for _ in range(4)]
            rhs = [rng.randrange(2) for _ in rows]
            expected = {
                x
                for x in range(8)
                if all((row & x).bit_count() % 2 == b for row, b in zip(rows, rhs))
            }
            answer = math["linear_equations_gf2"](rows, rhs, 3)
            rank, old_solution = math["solve_gf2"](rows, rhs, 3)
            if not expected:
                self.assertIsNone(answer)
                self.assertIsNone(old_solution)
            else:
                solution, basis = answer
                span = {solution}
                for value in basis:
                    span |= {x ^ value for x in span}
                self.assertEqual(span, expected)
                self.assertEqual(rank, 3 - len(basis))
                self.assertEqual(solution, old_solution)
        for n in (1, 2, 4, 8):
            a, b = (
                [rng.randrange(-10, 10) for _ in range(n)],
                [rng.randrange(-10, 10) for _ in range(n)],
            )
            for mod in (9, MOD):
                expected = [
                    sum(a[i] * b[i ^ k] for i in range(n)) % mod for k in range(n)
                ]
                self.assertEqual(math["xor_convolution"](a, b, mod), expected)
                transformed = math["walsh_hadamard"](a, mod=mod)
                self.assertEqual(
                    math["walsh_hadamard"](transformed, True, mod), [x % mod for x in a]
                )

    def test_bundled_official_samples(self):
        builder = runpy.run_path(str(ROOT / "verify" / "build.py"))
        count = 0
        for problem in builder["problems"]():
            source = builder["bundle"](problem)
            self.assertNotIn("from cp_snippet_palette", source)
            for sample in sorted((ROOT / "verify" / "samples" / problem).glob("*.in")):
                with self.subTest(problem=problem, sample=sample.name):
                    data = sample.read_bytes()
                    process = subprocess.run(
                        [sys.executable, "-B", "-I", "-c", source],
                        input=data,
                        capture_output=True,
                        timeout=15,
                    )
                    self.assertEqual(
                        process.returncode, 0, process.stderr.decode(errors="replace")
                    )
                    self.check_sample(problem, data.decode(), process.stdout.decode())
                    count += 1
        self.assertEqual(count, 23)

    def check_sample(self, problem, data, output):
        lines = [list(map(int, row.split())) for row in data.splitlines()]
        if problem == "queue_operate_all_composite":
            queue, expected = deque(), []
            for query in lines[1:]:
                if query[0] == 0:
                    queue.append(query[1:])
                elif query[0] == 1:
                    queue.popleft()
                else:
                    value = query[1]
                    for a, b in queue:
                        value = (a * value + b) % MOD
                    expected.append(value)
            self.assertEqual(list(map(int, output.split())), expected)
        elif problem == "segment_add_get_min":
            n = lines[0][0]
            segments, expected = lines[1 : n + 1], []
            for query in lines[n + 1 :]:
                if query[0] == 0:
                    segments.append(query[1:])
                else:
                    x = query[1]
                    values = [a * x + b for l, r, a, b in segments if l <= x < r]
                    expected.append(str(min(values)) if values else "INFINITY")
            self.assertEqual(output.split(), expected)
        elif problem == "biconnected_components":
            answer = [list(map(int, row.split())) for row in output.splitlines()]
            self.assertEqual(answer[0][0], len(answer) - 1)
            for row in answer[1:]:
                self.assertEqual(row[0], len(set(row[1:])))
            self.assertEqual(
                {frozenset(row[1:]) for row in answer[1:]},
                bcc_naive(lines[0][0], lines[1:]),
            )
        elif problem == "assignment":
            a = lines[1:]
            values = list(map(int, output.split()))
            self.assertEqual(sorted(values[1:]), list(range(len(a))))
            best = min(
                sum(a[i][j] for i, j in enumerate(p))
                for p in permutations(range(len(a)))
            )
            self.assertEqual(values[0], best)
            self.assertEqual(sum(a[i][j] for i, j in enumerate(values[1:])), best)
        elif problem in ("matrix_det", "matrix_rank"):
            a = lines[1:]
            expected = (
                determinant_naive(a, MOD)
                if problem == "matrix_det"
                else rank_naive(a, MOD)
            )
            self.assertEqual(int(output), expected)
        elif problem == "inverse_matrix":
            a, n = lines[1:], lines[0][0]
            if determinant_naive(a, MOD) == 0:
                self.assertEqual(output.strip(), "-1")
            else:
                inverse = [list(map(int, row.split())) for row in output.splitlines()]
                self.assertEqual([len(row) for row in inverse], [n] * n)
                for i in range(n):
                    for j in range(n):
                        self.assertEqual(
                            sum(a[i][k] * inverse[k][j] for k in range(n)) % MOD,
                            int(i == j),
                        )
        elif problem.startswith("system_of_linear_equations"):
            n, m = lines[0]
            if problem.endswith("mod_2"):
                raw = data.splitlines()
                a, b, mod = (
                    [list(map(int, row)) for row in raw[1 : n + 1]],
                    list(map(int, raw[n + 1])),
                    2,
                )
                answer = [[int(x) for x in row] for row in output.splitlines()[1:]]
            else:
                a, b, mod = lines[1 : n + 1], lines[n + 1], MOD
                answer = [
                    list(map(int, row.split())) for row in output.splitlines()[1:]
                ]
            rank = rank_naive(a, mod)
            augmented_rank = rank_naive(
                [row + [value] for row, value in zip(a, b)], mod
            )
            if augmented_rank > rank:
                self.assertEqual(output.strip(), "-1")
                return
            self.assertEqual(int(output.splitlines()[0]), m - rank)
            self.assertEqual(len(answer), m - rank + 1)
            self.assertEqual([len(row) for row in answer], [m] * len(answer))
            self.assertEqual(rank_naive(answer[1:], mod), m - rank)
            for index, vector in enumerate(answer):
                for row, value in zip(a, b):
                    self.assertEqual(
                        sum(x * y for x, y in zip(row, vector)) % mod,
                        value if index == 0 else 0,
                    )
        elif problem == "bitwise_xor_convolution":
            a, b = lines[1:]
            expected = [
                sum(a[i] * b[i ^ k] for i in range(len(a))) % MOD for k in range(len(a))
            ]
            self.assertEqual(list(map(int, output.split())), expected)
        else:
            self.fail("missing sample validator: " + problem)


if __name__ == "__main__":
    unittest.main()
