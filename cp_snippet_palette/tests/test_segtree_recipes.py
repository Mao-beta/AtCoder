"""派生セグ木の使用例・配列との比較・モノイド/作用則を小規模入力で確認する。"""

import ast
import json
from functools import reduce
from itertools import groupby
from math import gcd
from pathlib import Path
import random
import runpy
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).absolute().parents[1]
MONO = runpy.run_path(str(ROOT / "library/structures/segtree_monoids.py"))
LAZY = runpy.run_path(str(ROOT / "library/structures/lazy_segtree_actions.py"))


def max_subarray(a, empty=True):
    identity = 0 if empty else -float("inf")
    prefix = max([identity] + [sum(a[:i]) for i in range(1, len(a) + 1)])
    suffix = max([identity] + [sum(a[i:]) for i in range(len(a))])
    best = max(
        [identity]
        + [sum(a[i:j]) for i in range(len(a)) for j in range(i + 1, len(a) + 1)]
    )
    return sum(a), prefix, suffix, best


def brackets(a):
    balances = [sum(1 if c == "(" else -1 for c in a[:i]) for i in range(len(a) + 1)]
    return balances[-1], min(balances), max(balances)


def affine(a, mod=17):
    # x=0とx=1への適用結果から、合成後の切片・傾きを復元する。
    zero, one = 0, 1
    for slope, intercept in a:
        zero = (slope * zero + intercept) % mod
        one = (slope * one + intercept) % mod
    return (one - zero) % mod, zero


def matrix(a, mod=17):
    out = [[1, 0], [0, 1]]
    for v in a:
        b = [v[:2], v[2:]]
        out = [
            [sum(out[i][k] * b[k][j] for k in range(2)) % mod for j in range(2)]
            for i in range(2)
        ]
    return out[0][0], out[0][1], out[1][0], out[1][1]


def top2(a):
    values = sorted(set(a), reverse=True)
    first = (values[0], a.count(values[0])) if values else (None, 0)
    second = (values[1], a.count(values[1])) if len(values) > 1 else (None, 0)
    return first + second


def min_count(a):
    return (min(a), a.count(min(a))) if a else (float("inf"), 0)


def max_count(a):
    return (max(a), a.count(max(a))) if a else (-float("inf"), 0)


def inversions(a):
    return (
        a.count(0),
        a.count(1),
        sum(a[i] > a[j] for i in range(len(a)) for j in range(i + 1, len(a))),
    )


def runs(a):
    result = [len(a)]
    for bit in (0, 1):
        prefix = next((i for i, v in enumerate(a) if v != bit), len(a))
        suffix = next((i for i, v in enumerate(reversed(a)) if v != bit), len(a))
        best = max([0] + [len(list(g)) for v, g in groupby(a) if v == bit])
        result.extend((prefix, suffix, best))
    return tuple(result)


def digits(a):
    return int("".join(map(str, a)) or "0") % 97


def span(a):
    possible = {0}
    for value in a:
        possible |= {x ^ value for x in possible}
    return possible


def static_cases():
    numeric = [3, -1, 4, -1, 2]
    specs = [
        ("range_sum", numeric, {}, sum),
        ("range_min", numeric, {}, lambda a: min(a, default=float("inf"))),
        ("range_max", numeric, {}, lambda a: max(a, default=-float("inf"))),
        ("range_gcd", [6, 10, 14, 0, 18], {}, lambda a: reduce(gcd, a, 0)),
        ("range_xor", [3, 5, 6, 0, 9], {}, lambda a: reduce(int.__xor__, a, 0)),
        ("range_or", [3, 5, 6, 0, 9], {}, lambda a: reduce(int.__or__, a, 0)),
        ("range_and", [3, 5, 6, 0, 9], {}, lambda a: reduce(int.__and__, a, -1)),
        ("range_min_count", numeric, {}, min_count),
        ("range_max_count", numeric, {}, max_count),
        ("range_top2", numeric, {}, top2),
        ("range_max_subarray", numeric, {}, max_subarray),
        (
            "range_max_subarray",
            numeric,
            {"allow_empty": False},
            lambda a: max_subarray(a, False),
        ),
        ("range_brackets", list("(()))"), {}, brackets),
        (
            "range_affine_composite",
            [(2, 1), (0, 3), (4, 5), (1, 0), (3, 2)],
            {"mod": 17},
            affine,
        ),
        (
            "range_matrix_product",
            [(1, 2, 3, 4), (0, 1, 1, 0), (2, 0, 1, 1)],
            {"mod": 17},
            matrix,
        ),
        ("range_xor_basis", [3, 5, 6, 9, 0], {"bits": 4}, None),
        ("semigroup_segtree", numeric, {"OP": min}, lambda a: min(a) if a else None),
    ]
    return specs


def lazy_cases():
    # 更新関数は配列の要素へ直接適用し、内部ノードの式から独立させる。
    a = [3, -1, 4, -1, 2]
    add = lambda x, f, i: x + f
    assign = lambda x, f, i: x if f is None else f
    linear = lambda x, f, i: (f[0] * x + f[1]) % 17
    pair = [(1, 3), (2, 4), (5, 0), (1, 2), (4, 3)]
    return [
        ("range_add_sum", a, {}, sum, [-2, 0, 3], add),
        ("range_assign_sum", a, {}, sum, [None, 0, -3, 2], assign),
        (
            "range_affine_sum",
            a,
            {"mod": 17},
            lambda a: sum(a) % 17,
            [(2, 3), (0, 0), (-1, 2), (1, 0)],
            linear,
        ),
        (
            "range_add_min",
            a,
            {},
            lambda a: min(a, default=float("inf")),
            [-2, 0, 3],
            add,
        ),
        (
            "range_add_max",
            a,
            {},
            lambda a: max(a, default=-float("inf")),
            [-2, 0, 3],
            add,
        ),
        ("range_add_min_count", a, {}, min_count, [-2, 0, 3], add),
        (
            "range_affine_minmax",
            a,
            {},
            lambda a: (min(a, default=float("inf")), max(a, default=-float("inf"))),
            [(2, 3), (0, 0), (-1, 2), (1, 0)],
            lambda x, f, i: f[0] * x + f[1],
        ),
        (
            "range_clamp_minmax",
            a,
            {},
            lambda a: (min(a, default=float("inf")), max(a, default=-float("inf"))),
            [(-2, 2), (0, 0), (-float("inf"), 3), (4, float("inf"))],
            lambda x, f, i: min(max(x, f[0]), f[1]),
        ),
        (
            "range_flip_inversions",
            [1, 0, 1, 1, 0],
            {},
            inversions,
            [False, True],
            lambda x, f, i: 1 - x if f else x,
        ),
        (
            "range_binary_runs",
            [1, 0, 1, 1, 0],
            {},
            runs,
            [(0, 1), (1, 0), (0, 0), (1, 1)],
            lambda x, f, i: f[x],
        ),
        (
            "range_flip_brackets",
            list("(()))"),
            {},
            brackets,
            [False, True],
            lambda x, f, i: (")" if x == "(" else "(") if f else x,
        ),
        (
            "range_affine_sum_squares",
            a,
            {"mod": 17},
            lambda a: (sum(a) % 17, sum(x * x for x in a) % 17),
            [(2, 3), (0, 0), (-1, 2), (1, 0)],
            linear,
        ),
        (
            "range_pair_add_product",
            pair,
            {"mod": 17},
            lambda a: (
                sum(x for x, y in a) % 17,
                sum(y for x, y in a) % 17,
                sum(x * y for x, y in a) % 17,
            ),
            [(2, 3), (0, 0), (-1, 2)],
            lambda x, f, i: ((x[0] + f[0]) % 17, (x[1] + f[1]) % 17),
        ),
        (
            "range_index_affine_sum",
            a,
            {},
            sum,
            [(2, 3, -1), (0, -2, 3), (1, 0, 0)],
            lambda x, f, i: f[0] * x + f[1] * i + f[2],
        ),
        (
            "range_digit_assign",
            [1, 2, 3, 4, 5],
            {"mod": 97},
            digits,
            [None, 0, 9, 2],
            assign,
        ),
        ("range_assign_max_subarray", a, {}, max_subarray, [None, 0, -3, 2], assign),
        (
            "range_assign_max_subarray",
            a,
            {"allow_empty": False},
            lambda a: max_subarray(a, False),
            [None, 0, -3, 2],
            assign,
        ),
        (
            "range_add_gcd",
            [6, 10, 14, 0, -18],
            {},
            lambda a: reduce(gcd, a, 0),
            [-6, 0, 3],
            add,
        ),
    ]


class SegtreeRecipeTests(unittest.TestCase):
    def test_atcoder_official_samples(self):
        builder = runpy.run_path(str(ROOT / "verify/build.py"))
        samples = json.loads(
            (ROOT / "verify/atcoder_samples/segtree_recipes.json").read_text(
                encoding="utf8"
            )
        )
        self.assertTrue(set(samples).issubset(builder["problems"](True)))
        with tempfile.TemporaryDirectory(dir=str(ROOT.parent)) as folder:
            path = Path(folder) / "main.py"
            for problem, data in samples.items():
                code = builder["bundle"](problem, atcoder=True)
                self.assertIn(data["url"], code)
                path.write_text(code, encoding="utf8")
                for i, sample in enumerate(data["samples"]):
                    with self.subTest(problem=problem, sample=i):
                        result = subprocess.run(
                            [sys.executable, "-I", str(path)],
                            input=sample["input"],
                            text=True,
                            capture_output=True,
                            timeout=15,
                        )
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(
                            result.stdout.split(), sample["output"].split()
                        )

    def test_usage_examples(self):
        for filename in ["segtree_monoids", "lazy_segtree_actions"]:
            path = ROOT / "library/structures" / (filename + ".py")
            ns = runpy.run_path(str(path))
            doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf8")))
            code = "\n".join(
                line[4:] for line in doc.splitlines() if line.startswith("    ")
            )
            lines = code.splitlines()
            for node in ast.parse(code).body:
                line = lines[node.end_lineno - 1]
                if (
                    "# =>" not in line
                    and node.end_lineno < len(lines)
                    and lines[node.end_lineno].startswith("# =>")
                ):
                    line = lines[node.end_lineno]
                if isinstance(node, ast.Expr) and "# =>" in line:
                    actual = eval(
                        compile(ast.Expression(node.value), filename, "eval"), ns
                    )
                    self.assertEqual(
                        actual,
                        ast.literal_eval(line.split("# =>", 1)[1]),
                        (filename, line),
                    )
                else:
                    exec(
                        compile(
                            ast.Module(body=[node], type_ignores=[]), filename, "exec"
                        ),
                        ns,
                    )

    def test_point_updates_and_queries(self):
        for name, values, kwargs, oracle in static_cases():
            with self.subTest(name=name, kwargs=kwargs):
                a = values[:]
                seg = MONO[name](a, **kwargs)
                for l, r in [(0, 0), (0, len(a)), (1, len(a) - 1), (len(a), len(a))]:
                    if oracle:
                        self.assertEqual(seg.prod(l, r), oracle(a[l:r]))
                    else:
                        self.assertEqual(span(seg.prod(l, r)), span(a[l:r]))
                a[1] = a[-1]
                seg.set(1, a[-1])
                self.assertEqual(seg.get(1), a[1])
                self.assertEqual(seg.to_list(), a)
                if oracle:
                    self.assertEqual(seg.all_prod(), oracle(a))
                else:
                    self.assertEqual(seg.max_xor(0, len(a)), max(span(a)))
                    self.assertEqual(1 << seg.rank(0, len(a)), len(span(a)))

    def test_range_updates_against_array(self):
        rng = random.Random(813)
        for name, values, kwargs, oracle, updates, apply in lazy_cases():
            with self.subTest(name=name, kwargs=kwargs):
                seg = LAZY[name](values, **kwargs)
                a = seg.to_list()
                # 代入の0・負数、重なった非可換更新、点代入、片端・空区間を混ぜる。
                for step in range(24):
                    l, r = sorted(
                        [rng.randrange(len(a) + 1), rng.randrange(len(a) + 1)]
                    )
                    f = updates[step % len(updates)]
                    if step % 6 == 0:
                        l, r = 0, len(a)
                    seg.apply(l, r, f)
                    a[l:r] = [apply(x, f, i) for i, x in enumerate(a[l:r], l)]
                    if step % 5 == 0:
                        p = step % len(a)
                        seg.apply_point(p, f)
                        a[p] = apply(a[p], f, p)
                    if step % 7 == 0:
                        seg.set(2, values[0])
                        a[2] = seg.get(2)
                    ql, qr = sorted(
                        [rng.randrange(len(a) + 1), rng.randrange(len(a) + 1)]
                    )
                    self.assertEqual(seg.prod(ql, qr), oracle(a[ql:qr]), (step, ql, qr))
                    self.assertEqual(seg.all_prod(), oracle(a), step)
                    if step % 4 == 0:
                        self.assertEqual(seg.to_list(), a, step)

    def test_monoid_and_action_laws(self):
        for name, values, kwargs, _ in static_cases():
            with self.subTest(name=name):
                seg = MONO[name](values, **kwargs)
                x, y, z = [seg.d[seg.size + i] for i in range(3)]
                self.assertEqual(seg.op(seg.op(x, y), z), seg.op(x, seg.op(y, z)))
                self.assertEqual(seg.op(x, seg.e), x)
                self.assertEqual(seg.op(seg.e, x), x)
        for name, values, kwargs, _, updates, _ in lazy_cases():
            with self.subTest(name=name, kwargs=kwargs):
                seg = LAZY[name](values, **kwargs)
                x, y, z = [seg.d[seg.size + i] for i in range(3)]
                self.assertEqual(seg.op(seg.op(x, y), z), seg.op(x, seg.op(y, z)))
                self.assertEqual(seg.op(seg.e, x), x)
                self.assertEqual(seg.op(x, seg.e), x)
                self.assertEqual(seg.mapping(seg.identity, x), x)
                for f in updates:
                    self.assertEqual(seg.mapping(f, seg.e), seg.e)
                    self.assertEqual(
                        seg.mapping(f, seg.op(x, y)),
                        seg.op(seg.mapping(f, x), seg.mapping(f, y)),
                    )
                    for g in updates:
                        self.assertEqual(
                            seg.mapping(seg.composition(f, g), x),
                            seg.mapping(f, seg.mapping(g, x)),
                        )

    def test_empty_and_boundary_search(self):
        for name, values, kwargs, _ in static_cases():
            seg = MONO[name]([], **kwargs)
            self.assertEqual(seg.prod(0, 0), seg.all_prod())
            self.assertEqual(seg.to_list(), [])
            self.assertEqual(seg.max_right(0, lambda x: True), 0)
        for name, values, kwargs, oracle, updates, _ in lazy_cases():
            seg = LAZY[name]([], **kwargs)
            for f in updates:
                seg.apply(0, 0, f)
            self.assertEqual(seg.all_prod(), oracle([]))
            self.assertEqual(seg.to_list(), [])
            self.assertEqual(seg.min_left(0, lambda x: True), 0)
        seg = LAZY["range_add_sum"]([1, 2, 3, 4])
        seg.apply(0, 4, 1)
        self.assertEqual(seg.max_right(0, lambda x: x <= 9), 3)
        self.assertEqual(seg.min_left(4, lambda x: x <= 9), 2)
        seg = LAZY["range_binary_runs"]("001110")
        self.assertEqual(seg.max_right(0, lambda x: x[6] <= 2), 4)
        self.assertEqual(seg.min_left(6, lambda x: x[6] <= 2), 3)

    def test_convenience_and_modulus_options(self):
        seg = LAZY["range_binary_runs"]("001110")
        seg.flip(0, 2)
        seg.assign(1, 4, 0)
        self.assertEqual(seg.to_list(), [1, 0, 0, 0, 1, 0])
        self.assertEqual(seg.longest(0, 6, 0), 3)
        seg = LAZY["range_index_affine_sum"]([0] * 6)
        seg.add_progression(1, 5, 2, 3)
        seg.assign_progression(2, 4, 10, -1)
        self.assertEqual(seg.to_list(), [0, 2, 10, 9, 11, 0])
        seg = LAZY["range_clamp_minmax"]([-5, 2, 8])
        seg.chmax(0, 3, 0)
        seg.chmin(0, 3, 4)
        seg.assign(1, 2, -3)
        self.assertEqual(seg.to_list(), [0, -3, 4])
        for namespace, name in [
            (MONO, "range_brackets"),
            (LAZY, "range_flip_brackets"),
        ]:
            seg = namespace[name]("(()())")
            self.assertTrue(seg.balanced(0, 6))
            self.assertFalse(seg.balanced(0, 3))
        seg = LAZY["range_affine_sum_squares"]([10**12, -2], mod=0)
        seg.apply(0, 2, (-2, 3))
        a = [-2 * 10**12 + 3, 7]
        self.assertEqual(seg.all_prod(), (sum(a), sum(x * x for x in a)))
        seg = LAZY["range_digit_assign"]([1, 0, 1, 1], mod=12, base=2)
        seg.apply(1, 3, 1)
        self.assertEqual(seg.all_prod(), 15 % 12)
        seg = MONO["range_affine_composite"]([(2, 1), (3, 4)], mod=0)
        self.assertEqual(seg.all_prod(), (6, 7))
        seg = MONO["range_xor_basis"]([15, 8, 12, 3], bits=4)
        self.assertEqual(seg.max_xor(1, 4, 2), max(x ^ 2 for x in span([8, 12, 3])))


if __name__ == "__main__":
    unittest.main()
