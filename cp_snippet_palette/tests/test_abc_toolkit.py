"""ABC向け追加部品を小規模な全列挙・公式サンプル・使用例で確認する。"""

import ast
from collections import Counter, deque
from itertools import product
import json
from math import gcd
from pathlib import Path
import random
import runpy
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).absolute().parents[1]
FILES = [
    "graphs/functional_graph",
    "graphs/graph_recipes",
    "structures/xor_dsu",
    "structures/fenwick_multiset",
    "structures/dynamic_mex",
    "basic/intervals",
    "basic/subarray_count",
    "basic/digit_dp",
    "basic/knapsack_extra",
    "strings/subsequence",
    "basic/grid_search",
    "math/integer_count",
]
MODULES = {
    name: runpy.run_path(str(ROOT / "library" / (name + ".py"))) for name in FILES
}


class ABCToolkitTests(unittest.TestCase):
    def test_usage_examples(self):
        for name, namespace in MODULES.items():
            path = ROOT / "library" / (name + ".py")
            doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf8")))
            code = "\n".join(
                line[4:] for line in doc.splitlines() if line.startswith("    ")
            )
            lines = code.splitlines()
            scope = namespace.copy()
            for node in ast.parse(code).body:
                line = lines[node.end_lineno - 1]
                if (
                    "# =>" not in line
                    and node.end_lineno < len(lines)
                    and lines[node.end_lineno].startswith("# =>")
                ):
                    line = lines[node.end_lineno]
                with self.subTest(file=name, line=node.lineno):
                    if isinstance(node, ast.Expr) and "# =>" in line:
                        value = eval(
                            compile(ast.Expression(node.value), name, "eval"), scope
                        )
                        self.assertEqual(
                            value, ast.literal_eval(line.split("# =>", 1)[1].strip())
                        )
                    else:
                        exec(compile(ast.Module([node], []), name, "exec"), scope)

    def test_functional_graph(self):
        cls = MODULES["graphs/functional_graph"]["FunctionalGraph"]
        rng = random.Random(401)
        for n in range(1, 13):
            nxt = [rng.randrange(n) for _ in range(n)]
            fg = cls(nxt)
            for source in range(n):
                order, seen, v = [], {}, source
                while v not in seen:
                    seen[v] = len(order)
                    order.append(v)
                    v = nxt[v]
                start = seen[v]
                self.assertEqual(fg.reachable_count(source), len(order))
                for target in range(n):
                    self.assertEqual(fg.distance(source, target), seen.get(target, -1))
                for k in [0, 1, n, 3 * n, 10**50]:
                    expected = (
                        order[k]
                        if k < len(order)
                        else order[start + (k - start) % (len(order) - start)]
                    )
                    self.assertEqual(fg.jump(source, k), expected)
        self.assertEqual(cls([]).cycles, [])

    def test_graph_recipes(self):
        m = MODULES["graphs/graph_recipes"]
        rng = random.Random(402)
        graph = [
            [j for j in range(i + 1, 14) if rng.randrange(4) == 0] for i in range(14)
        ]
        queries = list(product(range(14), repeat=2))
        expected = []
        for source, target in queries:
            seen, queue = {source}, [source]
            for v in queue:
                for w in graph[v]:
                    if w not in seen:
                        seen.add(w)
                        queue.append(w)
            expected.append(target in seen)
        self.assertEqual(m["dag_reachability"](graph, queries, 7), expected)
        with self.assertRaises(ValueError):
            m["dag_reachability"]([[1], [0]], [])
        self.assertIsNone(m["bipartite_coloring"]([[1, 2], [0, 2], [0, 1]]))
        self.assertIsNone(m["bipartite_coloring"]([[0]]))
        self.assertEqual(m["bipartite_coloring"]([[], []])[1], [(1, 0), (1, 0)])
        self.assertEqual(m["bfs_path_count"]([[1, 1], []], 0), ([0, 1], [1, 2]))
        dist, parent = m["multi_source_bfs"]([[1], [2], [], []], [0, 0])
        self.assertEqual((dist, parent), ([0, 1, 2, -1], [-1, 0, 1, -1]))

    def test_xor_dsu(self):
        cls = MODULES["structures/xor_dsu"]["XorDSU"]
        rng = random.Random(403)
        hidden = [rng.randrange(16) for _ in range(12)]
        uf = cls(12)
        for a, b in [(i // 2, i) for i in range(1, 9)] + [(9, 10)]:
            leader = uf.merge(a, b, hidden[a] ^ hidden[b])
            self.assertEqual(leader, uf.leader(a))
        for group in uf.groups():
            for a, b in product(group, repeat=2):
                self.assertEqual(uf.diff(a, b), hidden[a] ^ hidden[b])
        answer = uf.minimum_sum_values()
        for group in uf.groups():
            self.assertEqual(
                sum(answer[v] for v in group),
                min(sum(hidden[v] ^ x for v in group) for x in range(16)),
            )
        with self.assertRaises(ValueError):
            uf.merge(0, 1, hidden[0] ^ hidden[1] ^ 1)
        self.assertEqual(uf.diff(0, 1), hidden[0] ^ hidden[1])
        with self.assertRaises(ValueError):
            uf.diff(0, 11)

    def test_fenwick_and_mex(self):
        bag_cls = MODULES["structures/fenwick_multiset"]["FenwickMultiset"]
        mex_cls = MODULES["structures/dynamic_mex"]["DynamicMex"]
        rng, a = random.Random(404), [0, 1, 1, 3, 4, 5, 7]
        bag, mex = bag_cls(range(-3, 12), a), mex_cls(7, a)
        for _ in range(50):
            i, x = rng.randrange(len(a)), rng.randrange(-3, 12)
            bag.discard(a[i])
            mex.discard(a[i])
            a[i] = x
            bag.add(x)
            mex.add(x)
            ordered = sorted(a)
            self.assertEqual(bag.total, sum(a))
            for k in range(len(a) + 1):
                self.assertEqual(bag.sum_smallest(k), sum(ordered[:k]))
                self.assertEqual(bag.sum_largest(k), sum(ordered[len(a) - k :]))
                if k < len(a):
                    self.assertEqual(bag.kth(k), ordered[k])
            self.assertEqual(bag.sum_abs(x), sum(abs(v - x) for v in a))
            self.assertEqual(bag.bisect_left(x), sum(v < x for v in a))
            self.assertEqual(bag.bisect_right(x), sum(v <= x for v in a))
            self.assertEqual(bag.count(x), a.count(x))
            self.assertEqual(mex.mex(), next(i for i in range(8) if i not in a))
        self.assertEqual(bag.discard(999), 0)
        self.assertEqual(bag_cls([]).sum_smallest(0), 0)
        self.assertIsNone(mex_cls(1, [0, 1]).mex())
        self.assertEqual(mex_cls(0).mex(), 0)

    def test_intervals(self):
        m, rng = MODULES["basic/intervals"], random.Random(405)
        for _ in range(20):
            ranges = []
            for i in range(4):
                a, b = sorted([rng.randrange(-2, 4), rng.randrange(-2, 4)])
                ranges.append((a, b))
            valid = any(
                len(set(xs)) == len(xs)
                for xs in product(*(range(l, r + 1) for l, r in ranges))
            )
            result = m["assign_distinct_in_intervals"](ranges)
            self.assertEqual(result is not None, valid)
            if result is not None:
                self.assertEqual(len(set(result)), len(result))
                self.assertTrue(all(l <= x <= r for x, (l, r) in zip(result, ranges)))
            counts = Counter(sum(l <= x < r for l, r in ranges) for x in range(-2, 4))
            expected = [0] + [counts[i] for i in range(1, 5)]
            self.assertEqual(m["covered_lengths"](ranges), expected)
            self.assertEqual(m["interval_union_length"](ranges), sum(expected))
        tasks = [(0, 3), (1, 2), (2, 4), (3, 6), (4, 5)]
        selected = m["schedule_intervals"](tasks)
        optimum = 0
        for mask in range(1 << len(tasks)):
            picked = sorted(tasks[i] for i in range(len(tasks)) if mask >> i & 1)
            if all(picked[i - 1][1] <= picked[i][0] for i in range(1, len(picked))):
                optimum = max(optimum, len(picked))
        self.assertEqual(len(selected), optimum)

    def test_subarrays(self):
        m, rng = MODULES["basic/subarray_count"], random.Random(406)
        for _ in range(20):
            a = [rng.randrange(-2, 4) for _ in range(7)]
            ranges = [a[l:r] for l in range(len(a)) for r in range(l + 1, len(a) + 1)]
            self.assertEqual(
                m["count_subarrays_sum"](a, 2), sum(sum(x) == 2 for x in ranges)
            )
            self.assertEqual(
                m["count_subarrays_minmax"](a, -1, 2),
                sum(min(x) == -1 and max(x) == 2 for x in ranges),
            )
            self.assertEqual(
                m["count_subarrays_distinct_exact"](a, 2),
                sum(len(set(x)) == 2 for x in ranges),
            )
            self.assertEqual(
                m["count_subarrays_distinct_at_most"](a, 2),
                sum(len(set(x)) <= 2 for x in ranges),
            )
            self.assertEqual(m["sum_subarray_min"](a), sum(map(min, ranges)))
            self.assertEqual(m["sum_subarray_max"](a), sum(map(max, ranges)))
            b = [abs(x) for x in a]
            self.assertEqual(
                m["count_subarrays_sum_leq"](b, 3),
                sum(sum(b[l:r]) <= 3 for l in range(7) for r in range(l + 1, 8)),
            )
        with self.assertRaises(ValueError):
            m["count_subarrays_sum_leq"]([-1], 0)
        self.assertEqual(m["count_subarrays_distinct_exact"]([1], 0), 0)

    def test_digit_dp(self):
        m = MODULES["basic/digit_dp"]
        for bound in [0, 1, 9, 10, 19, 80, 123]:
            values = [str(v) for v in range(bound + 1)]
            for k in range(4):
                expected = sum(sum(c != "0" for c in s) == k for s in values)
                self.assertEqual(m["count_nonzero_digits"](str(bound), k), expected)
                self.assertEqual(m["count_nonzero_digits"](bound, k, 7), expected % 7)
            for d in [1, 3, 7]:
                self.assertEqual(
                    m["count_digit_sum_mod"](bound, d),
                    sum(sum(map(int, s)) % d == 0 for s in values) - 1,
                )
            for forbidden in [{4, 9}, {0}, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, set()]:
                self.assertEqual(
                    m["count_avoiding_digits"](bound, forbidden),
                    sum(not (set(map(int, s)) & forbidden) for s in values),
                )
            for digit in [0, 1, 9]:
                self.assertEqual(
                    m["count_digit_occurrences"](bound, digit),
                    sum(s.count(str(digit)) for s in values),
                )
        self.assertEqual(m["count_nonzero_digits"]("1" + "0" * 100, 1), 901)
        self.assertEqual(m["count_digit_occurrences"](-1, 0), 0)
        self.assertEqual(m["count_avoiding_digits"]("00010", {0}), 9)

    def test_knapsack(self):
        m, rng = MODULES["basic/knapsack_extra"], random.Random(407)
        for _ in range(15):
            items = [
                (rng.randrange(4), rng.randrange(6), rng.randrange(3)) for _ in range(4)
            ]
            capacity = 7
            best = max(
                sum(c * v for c, (w, v, limit) in zip(counts, items))
                for counts in product(*(range(c + 1) for w, v, c in items))
                if sum(c * w for c, (w, v, limit) in zip(counts, items)) <= capacity
            )
            self.assertEqual(m["bounded_knapsack"](items, capacity), best)
            single = [(w, v) for w, v, c in items]
            best01 = max(
                sum(v for bit, (w, v) in zip(bits, single) if bit)
                for bits in product([0, 1], repeat=4)
                if sum(w for bit, (w, v) in zip(bits, single) if bit) <= capacity
            )
            self.assertEqual(m["knapsack_by_value"](single, capacity), best01)
            values = [w for w, v in single]
            possible = {
                sum(v for bit, v in zip(bits, values) if bit)
                for bits in product([0, 1], repeat=4)
            }
            for target in range(9):
                result = m["subset_sum_restore"](values, target)
                self.assertEqual(result is not None, target in possible)
                if result is not None:
                    self.assertEqual(len(set(result)), len(result))
                    self.assertEqual(sum(values[i] for i in result), target)
                possible_two = {
                    sum(pair[bit] for pair, bit in zip(single, bits))
                    for bits in product([0, 1], repeat=4)
                }
                result = m["two_choice_sum"](single, target)
                self.assertEqual(result is not None, target in possible_two)
                if result is not None:
                    self.assertEqual(
                        sum(pair[bit] for pair, bit in zip(single, result)), target
                    )
        self.assertEqual(m["knapsack_unbounded"]([(2, 3), (3, 5)], 7), 11)
        self.assertEqual(m["bounded_knapsack"]([(0, -2, 5), (0, 3, 4)], 0), 12)

    def test_strings(self):
        m, rng = MODULES["strings/subsequence"], random.Random(408)
        matching = runpy.run_path(str(ROOT / "library/strings/matching.py"))
        for _ in range(20):
            a = "".join(rng.choice("abc") for _ in range(7))
            b = "".join(rng.choice("abc") for _ in range(rng.randrange(8)))
            subseqs = [
                "".join(c for bit, c in zip(bits, a) if bit)
                for bits in product([0, 1], repeat=len(a))
            ]
            self.assertEqual(m["count_distinct_subsequences"](a), len(set(subseqs)) - 1)
            self.assertEqual(m["count_subsequence"](a, "ab", 0), subseqs.count("ab"))
            self.assertEqual(
                m["smallest_subsequence"](a, 3), min(s for s in subseqs if len(s) == 3)
            )
            restored = m["lcs_restore"](a, b)
            self.assertEqual(len(restored), matching["lcs_length"](a, b))
            self.assertIsNotNone(m["subsequence_positions"](a, restored))
            self.assertIsNotNone(m["subsequence_positions"](b, restored))
            distance = matching["edit_distance"](a, b)
            for k in [0, 1, 2, 5, 10]:
                self.assertEqual(
                    m["edit_distance_bounded"](a, b, k), min(k + 1, distance)
                )
        self.assertEqual(m["edit_distance_bounded"]("", "abc", 3), 3)
        self.assertEqual(m["count_subsequence"]("", "", 1), 0)

    def test_grid(self):
        m = MODULES["basic/grid_search"]
        grid = ["..#", "...", "#.."]
        dist = m["grid_bfs"](grid, [(0, 0), (2, 2)])
        self.assertEqual(dist, [[0, 1, -1], [1, 2, 1], [-1, 1, 0]])
        path = m["grid_shortest_path"](grid, (0, 0), (2, 2))
        self.assertTrue(
            all(abs(a - c) + abs(b - d) == 1 for (a, b), (c, d) in zip(path, path[1:]))
        )
        self.assertIsNone(m["grid_shortest_path"]([".#."], (0, 0), (0, 2)))
        self.assertEqual(m["grid_min_turns"](["...."], (0, 0), (0, 3)), 0)
        self.assertEqual(m["grid_min_turns"]([".#."], (0, 0), (0, 2)), -1)
        self.assertEqual(m["grid_min_turns"](["."], (0, 0), (0, 0)), 0)
        self.assertEqual(m["grid_components"](["#.", ".#"])[1], [1, 1])
        self.assertEqual(m["grid_components"]([]), ([], []))

    def test_integer_count(self):
        m = MODULES["math/integer_count"]
        phi, mu = m["totient_sieve"](50), m["mobius_sieve"](50)
        for n in range(1, 51):
            self.assertEqual(phi[n], sum(gcd(n, x) == 1 for x in range(1, n + 1)))
            self.assertEqual(
                sum(mu[d] for d in range(1, n + 1) if n % d == 0), int(n == 1)
            )
            self.assertEqual(
                m["sum_floor_quotients"](n), sum(n // i for i in range(1, n + 1))
            )
        for a, b, mod in product(range(-3, 4), range(-3, 4), range(1, 8)):
            solutions = [x for x in range(mod) if (a * x - b) % mod == 0]
            result = m["linear_congruence"](a, b, mod)
            self.assertEqual(result is not None, bool(solutions))
            if result is not None:
                start, period = result
                self.assertEqual(list(range(start, mod, period)), solutions)

    def test_atcoder_samples(self):
        builder = runpy.run_path(str(ROOT / "verify/build.py"))
        samples = json.loads(
            (ROOT / "verify/atcoder_samples/abc_toolkit.json").read_text(
                encoding="utf8"
            )
        )
        self.assertEqual(len(samples), 17)
        with tempfile.TemporaryDirectory(dir=str(ROOT.parent)) as folder:
            path = Path(folder) / "main.py"
            for name, data in samples.items():
                source = builder["bundle"](name, atcoder=True)
                self.assertIn(data["url"], source)
                path.write_text(source, encoding="utf8")
                for i, sample in enumerate(data["samples"]):
                    with self.subTest(problem=name, sample=i):
                        result = subprocess.run(
                            [sys.executable, "-I", str(path)],
                            input=sample["input"],
                            text=True,
                            capture_output=True,
                            timeout=20,
                        )
                        self.assertEqual(result.returncode, 0, result.stderr)
                        actual, expected = (
                            result.stdout.split(),
                            sample["output"].split(),
                        )
                        if name == "abc271_d" and expected[0] == "Yes":
                            tokens = list(map(int, sample["input"].split()))
                            n, target = tokens[:2]
                            self.assertEqual(actual[0], "Yes")
                            self.assertEqual(len(actual[1]), n)
                            self.assertTrue(set(actual[1]) <= {"H", "T"})
                            self.assertEqual(
                                sum(
                                    tokens[2 + 2 * j + (c == "T")]
                                    for j, c in enumerate(actual[1])
                                ),
                                target,
                            )
                        elif name == "abc396_e" and expected != ["-1"]:
                            tokens = list(map(int, sample["input"].split()))
                            values = list(map(int, actual))
                            self.assertEqual(len(values), tokens[0])
                            self.assertTrue(all(v >= 0 for v in values))
                            for j in range(tokens[1]):
                                x, y, z = tokens[2 + 3 * j : 5 + 3 * j]
                                self.assertEqual(values[x - 1] ^ values[y - 1], z)
                            self.assertEqual(sum(values), sum(map(int, expected)))
                        else:
                            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
