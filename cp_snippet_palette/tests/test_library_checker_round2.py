"""第2弾50問。公式入力は提出コードを通し、独立した小規模計算で出力を検査する。"""

from collections import deque
from functools import lru_cache
from pathlib import Path
import random
import runpy
import subprocess
import sys
import unittest

ROOT = Path(__file__).absolute().parents[1]
MOD = 998244353
FIRST = {
    "queue_operate_all_composite",
    "segment_add_get_min",
    "biconnected_components",
    "assignment",
    "matrix_det",
    "matrix_rank",
    "inverse_matrix",
    "system_of_linear_equations",
    "system_of_linear_equations_mod_2",
    "bitwise_xor_convolution",
}


@lru_cache(None)
def lib(name):
    return runpy.run_path(str(ROOT / "library" / (name + ".py")))


def mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % MOD
    return c


def trim(a):
    a = [x % MOD for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def divmod_naive(a, b):
    a, b = trim(a), trim(b)
    q = [0] * max(0, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, MOD)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        x = a[-1] * inverse % MOD
        q[shift] = x
        for j, y in enumerate(b):
            a[shift + j] = (a[shift + j] - x * y) % MOD
        a = trim(a)
    return trim(q), a


def rank(a, mod):
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][j] % mod), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        x = pow(a[r][j], -1, mod)
        a[r] = [v * x % mod for v in a[r]]
        for i in range(r + 1, len(a)):
            x = a[i][j]
            a[i] = [(u - x * v) % mod for u, v in zip(a[i], a[r])]
        r += 1
    return r


def reachability(n, edges, directed=False):
    g = [[False] * n for _ in range(n)]
    for i in range(n):
        g[i][i] = True
    for u, v in edges:
        g[u][v] = True
        if not directed:
            g[v][u] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] |= g[i][k] and g[k][j]
    return g


def path_between(graph, s, t):
    queue = [[s]]
    seen = {s}
    for path in queue:
        if path[-1] == t:
            return path
        for v in graph[path[-1]]:
            if v not in seen:
                seen.add(v)
                queue.append(path + [v])
    return []


def matching_size(graph):
    @lru_cache(None)
    def solve(i, used):
        if i == len(graph):
            return 0
        return max(
            [solve(i + 1, used)]
            + [
                1 + solve(i + 1, used | (1 << v))
                for v in graph[i]
                if not (used >> v & 1)
            ]
        )

    return solve(0, 0)


def check_sample(pid, data, output):
    raw = data.splitlines()
    out = output.split()
    if pid == "two_sat":
        n = int(raw[0].split()[2])
        clauses = [list(map(int, line.split()))[:2] for line in raw[1:]]
        valid = lambda mask: all(
            any(bool(mask >> (abs(x) - 1) & 1) == (x > 0) for x in c) for c in clauses
        )
        if out == ["s", "UNSATISFIABLE"]:
            assert not any(valid(mask) for mask in range(1 << n))
        else:
            assert out[:3] == ["s", "SATISFIABLE", "v"] and out[-1] == "0"
            values = list(map(int, out[3:-1]))
            assert [abs(x) for x in values] == list(range(1, n + 1))
            assert valid(sum(1 << i for i, x in enumerate(values) if x > 0))
        return
    if pid == "longest_common_substring":
        s, t = raw
        a, b, c, d = map(int, out)
        assert 0 <= a <= b <= len(s) and 0 <= c <= d <= len(t)
        assert s[a:b] == t[c:d]
        assert b - a == max(
            (
                j - i
                for i in range(len(s) + 1)
                for j in range(i, len(s) + 1)
                if s[i:j] in t
            ),
            default=0,
        )
        return
    if pid == "enumerate_palindromes":
        s = raw[0]
        expected = []
        for center in range(2 * len(s) - 1):
            lengths = [
                r - l
                for l in range(len(s) + 1)
                for r in range(l, len(s) + 1)
                if l + r - 1 == center and s[l:r] == s[l:r][::-1]
            ]
            expected.append(max(lengths, default=0))
        assert list(map(int, out)) == expected
        return
    if pid in {"inverse_matrix_mod_2", "matrix_rank_mod_2", "matrix_product_mod_2"}:
        dims = list(map(int, raw[0].split()))
        n = dims[0]
        a = [list(map(int, row)) for row in raw[1 : n + 1]]
        if pid == "matrix_rank_mod_2":
            assert int(output) == rank(a, 2)
        elif pid == "inverse_matrix_mod_2":
            if rank(a, 2) < n:
                assert out == ["-1"]
            else:
                inv = [list(map(int, row)) for row in out]
                assert len(inv) == n and all(len(row) == n for row in inv)
                assert all(
                    sum(a[i][k] * inv[k][j] for k in range(n)) % 2 == int(i == j)
                    for i in range(n)
                    for j in range(n)
                )
        else:
            _, m, k = dims
            b = [list(map(int, row)) for row in raw[n + 1 :]]
            expected = [
                "".join(
                    str(sum(a[i][h] * b[h][j] for h in range(m)) % 2) for j in range(k)
                )
                for i in range(n)
            ]
            assert out == expected
        return
    rows = [list(map(int, row.split())) for row in raw]
    actual = list(map(int, out))
    expected = []
    if pid == "persistent_unionfind":
        n, q = rows[0]
        versions = {-1: list(range(n))}
        for i, (t, k, u, v) in enumerate(rows[1:]):
            a = versions[k][:]
            if t == 0:
                x, y = a[u], a[v]
                versions[i] = [x if value == y else value for value in a]
            else:
                expected.append(int(a[u] == a[v]))
    elif pid == "persistent_queue":
        versions = {-1: []}
        for i, row in enumerate(rows[1:]):
            a = versions[row[1]][:]
            if row[0] == 0:
                a.append(row[2])
            else:
                expected.append(a.pop(0))
            versions[i] = a
    elif pid == "deque_operate_all_composite":
        a = deque()
        for row in rows[1:]:
            t = row[0]
            if t == 0:
                a.appendleft(row[1:])
            elif t == 1:
                a.append(row[1:])
            elif t == 2:
                a.popleft()
            elif t == 3:
                a.pop()
            else:
                x = row[1]
                for b, c in a:
                    x = (b * x + c) % MOD
                expected.append(x)
    elif pid in {
        "range_affine_range_sum",
        "range_affine_point_get",
        "range_chmin_chmax_add_range_sum",
        "range_reverse_range_sum",
        "dynamic_sequence_range_affine_range_sum",
        "staticrmq",
        "range_kth_smallest",
        "static_range_frequency",
        "static_range_count_distinct",
    }:
        a = rows[1][:]
        for row in rows[2:]:
            t = row[0]
            if pid == "staticrmq":
                expected.append(min(a[row[0] : row[1]]))
                continue
            if pid == "range_kth_smallest":
                expected.append(sorted(a[row[0] : row[1]])[row[2]])
                continue
            if pid == "static_range_frequency":
                expected.append(a[row[0] : row[1]].count(row[2]))
                continue
            if pid == "static_range_count_distinct":
                expected.append(len(set(a[row[0] : row[1]])))
                continue
            if pid == "dynamic_sequence_range_affine_range_sum":
                if t == 0:
                    a.insert(row[1], row[2])
                    continue
                if t == 1:
                    a.pop(row[1])
                    continue
                l, r = row[1:3]
                if t == 2:
                    a[l:r] = a[l:r][::-1]
                elif t == 3:
                    a[l:r] = [(row[3] * x + row[4]) % MOD for x in a[l:r]]
                else:
                    expected.append(sum(a[l:r]) % MOD)
            elif pid == "range_reverse_range_sum":
                l, r = row[1:]
                if t == 0:
                    a[l:r] = a[l:r][::-1]
                else:
                    expected.append(sum(a[l:r]))
            elif pid == "range_chmin_chmax_add_range_sum":
                l, r = row[1:3]
                if t == 0:
                    a[l:r] = [min(x, row[3]) for x in a[l:r]]
                elif t == 1:
                    a[l:r] = [max(x, row[3]) for x in a[l:r]]
                elif t == 2:
                    a[l:r] = [x + row[3] for x in a[l:r]]
                else:
                    expected.append(sum(a[l:r]))
            elif t == 0:
                _, l, r, b, c = row
                a[l:r] = [(b * x + c) % MOD for x in a[l:r]]
            elif pid == "range_affine_point_get":
                expected.append(a[row[1]])
            else:
                expected.append(sum(a[row[1] : row[2]]) % MOD)
    elif pid == "point_set_range_composite":
        n, q = rows[0]
        a = rows[1 : n + 1]
        for t, l, r, x in rows[n + 1 :]:
            if t == 0:
                a[l] = [r, x]
            else:
                for b, c in a[l:r]:
                    x = (b * x + c) % MOD
                expected.append(x)
    elif pid == "line_add_get_min":
        n, q = rows[0]
        lines = rows[1 : n + 1]
        for row in rows[n + 1 :]:
            if row[0] == 0:
                lines.append(row[1:])
            else:
                expected.append(min(a * row[1] + b for a, b in lines))
    elif pid == "point_add_rectangle_sum":
        n, q = rows[0]
        points = rows[1 : n + 1]
        for row in rows[n + 1 :]:
            if row[0] == 0:
                points.append(row[1:])
            else:
                _, l, d, r, u = row
                expected.append(
                    sum(w for x, y, w in points if l <= x < r and d <= y < u)
                )
    elif pid == "set_xor_min":
        a = set()
        for t, x in rows[1:]:
            if t == 0:
                a.add(x)
            elif t == 1:
                a.discard(x)
            else:
                expected.append(min(x ^ y for y in a))
    elif pid in {
        "cycle_detection",
        "cycle_detection_undirected",
        "two_edge_connected_components",
        "scc",
    }:
        n, m = rows[0]
        edges = rows[1:]
        directed = pid in {"cycle_detection", "scc"}
        reach = reachability(n, edges, directed)
        if pid.startswith("cycle_detection"):
            if actual == [-1]:
                if directed:
                    assert not any(reach[v][u] for u, v in edges)
                else:
                    assert not any(
                        reachability(n, edges[:i] + edges[i + 1 :])[u][v]
                        for i, (u, v) in enumerate(edges)
                    )
            else:
                size = actual[0]
                assert size > 0
                if directed:
                    ids = actual[1:]
                    vertices = [edges[i][0] for i in ids]
                else:
                    vertices, ids = actual[1 : 1 + size], actual[1 + size :]
                assert len(ids) == size == len(set(ids)) == len(set(vertices))
                for i, eid in enumerate(ids):
                    u, v = vertices[i], vertices[(i + 1) % size]
                    assert edges[eid] == [u, v] or (
                        not directed and edges[eid] == [v, u]
                    )
            return
        groups = [list(map(int, row.split()))[1:] for row in output.splitlines()[1:]]
        assert actual[0] == len(groups) and sorted(
            x for g in groups for x in g
        ) == list(range(n))
        for row in output.splitlines()[1:]:
            values = list(map(int, row.split()))
            assert values[0] == len(values) - 1
        ids = {v: i for i, g in enumerate(groups) for v in g}
        if pid == "scc":
            assert all(
                (ids[u] == ids[v]) == (reach[u][v] and reach[v][u])
                for u in range(n)
                for v in range(n)
            )
            assert all(ids[u] <= ids[v] for u, v in edges)
        else:
            kept = [
                e
                for i, e in enumerate(edges)
                if reachability(n, edges[:i] + edges[i + 1 :])[e[0]][e[1]]
            ]
            connected = reachability(n, kept)
            assert all(
                (ids[u] == ids[v]) == connected[u][v]
                for u in range(n)
                for v in range(n)
            )
        return
    elif pid in {
        "jump_on_tree",
        "lca",
        "vertex_add_path_sum",
        "vertex_set_path_composite",
        "vertex_add_subtree_sum",
    }:
        n, q = rows[0]
        index = 1
        values = None
        if pid.startswith("vertex_"):
            if pid == "vertex_set_path_composite":
                values = rows[index : index + n]
                index += n
            else:
                values = rows[index][:]
                index += 1
        graph = [[] for _ in range(n)]
        if pid in {"lca", "vertex_add_subtree_sum"}:
            edges = [(u, p) for u, p in enumerate(rows[index], 1)]
            index += 1
        else:
            edges = rows[index : index + n - 1]
            index += n - 1
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        root_paths = [path_between(graph, 0, v) for v in range(n)]
        for row in rows[index:]:
            if pid == "lca":
                p1, p2 = (root_paths[v] for v in row)
                expected.append([x for x, y in zip(p1, p2) if x == y][-1])
            elif pid == "jump_on_tree":
                u, v, k = row
                path = path_between(graph, u, v)
                expected.append(path[k] if k < len(path) else -1)
            elif row[0] == 0:
                u = row[1]
                if pid == "vertex_set_path_composite":
                    values[u] = row[2:]
                else:
                    values[u] += row[2]
            elif pid == "vertex_add_subtree_sum":
                expected.append(
                    sum(values[v] for v in range(n) if row[1] in root_paths[v])
                )
            elif pid == "vertex_add_path_sum":
                expected.append(sum(values[v] for v in path_between(graph, *row[1:])))
            else:
                x = row[3]
                for v in path_between(graph, row[1], row[2]):
                    a, b = values[v]
                    x = (a * x + b) % MOD
                expected.append(x)
    elif pid == "bipartitematching":
        l, r, m = rows[0]
        edges = set(map(tuple, rows[1:]))
        graph = [[] for _ in range(l)]
        for u, v in edges:
            graph[u].append(v)
        pairs = list(zip(actual[1::2], actual[2::2]))
        assert actual[0] == len(pairs) == matching_size(graph)
        assert len({u for u, v in pairs}) == len(pairs) == len({v for u, v in pairs})
        assert all(p in edges for p in pairs)
        return
    elif pid in {"tree_diameter", "shortest_path", "minimum_spanning_tree"}:
        n = rows[0][0]
        edges = rows[1:]
        inf = 10**30
        d = [[inf] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for u, v, w in edges:
            d[u][v] = min(d[u][v], w)
            if pid != "shortest_path":
                d[v][u] = min(d[v][u], w)
        edge_weights = [row[:] for row in d]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        if pid == "shortest_path":
            _, _, s, t = rows[0]
            if d[s][t] == inf:
                assert actual == [-1]
            else:
                assert actual[0] == d[s][t] and actual[1] * 2 == len(actual) - 2
                pairs = list(zip(actual[2::2], actual[3::2]))
                cur = s
                total = 0
                for u, v in pairs:
                    assert u == cur and edge_weights[u][v] < inf
                    cur = v
                    total += edge_weights[u][v]
                assert cur == t and total == d[s][t]
        elif pid == "tree_diameter":
            length, size = actual[:2]
            path = actual[2:]
            assert size == len(path) == len(set(path)) and length == max(map(max, d))
            assert sum(edge_weights[u][v] for u, v in zip(path, path[1:])) == length
        else:
            used = {0}
            best = 0
            while len(used) < n:
                w, u, v = min(
                    (w, u, v) if u in used else (w, v, u)
                    for u, v, w in edges
                    if (u in used) != (v in used)
                )
                best += w
                used.add(v)
            chosen = [edges[i] for i in actual[1:]]
            assert len(chosen) == n - 1 and actual[0] == best == sum(
                e[2] for e in chosen
            )
            assert all(map(all, reachability(n, [(u, v) for u, v, w in chosen])))
        return
    elif pid == "area_of_union_of_rectangles":
        rects = rows[1:]
        xs = sorted({x for l, b, r, t in rects for x in (l, r)})
        ys = sorted({y for l, b, r, t in rects for y in (b, t)})
        expected = [
            sum(
                (xx - x) * (yy - y)
                for x, xx in zip(xs, xs[1:])
                for y, yy in zip(ys, ys[1:])
                if any(l <= x < r and b <= y < t for l, b, r, t in rects)
            )
        ]
    elif pid == "multipoint_evaluation":
        expected = [
            sum(c * pow(x, i, MOD) for i, c in enumerate(rows[1])) % MOD
            for x in rows[2]
        ]
    elif pid == "polynomial_interpolation":
        assert len(actual) == rows[0][0]
        assert [
            sum(c * pow(x, i, MOD) for i, c in enumerate(actual)) % MOD for x in rows[1]
        ] == rows[2]
        return
    elif pid == "polynomial_taylor_shift":
        from math import comb

        n, c = rows[0]
        a = rows[1]
        expected = [
            sum(a[j] * comb(j, i) * pow(c, j - i, MOD) for j in range(i, n)) % MOD
            for i in range(n)
        ]
    elif pid == "division_of_polynomials":
        q, r = divmod_naive(rows[1], rows[2])
        expected = [len(q), len(r)] + q + r
    elif pid == "inv_of_polynomials":
        a, b = rows[1:]
        x, y = a, b
        while y:
            x, y = y, divmod_naive(x, y)[1]
        if len(x) > 1:
            assert actual == [-1]
        else:
            assert actual[0] == len(actual) - 1 and (not actual[0] or actual[-1] != 0)
            assert (
                len(actual) - 1 < len(b)
                and divmod_naive(mul(a, actual[1:]), b)[1] == divmod_naive([1], b)[1]
            )
        return
    elif pid == "convolution_mod":
        expected = mul(rows[1], rows[2])
    elif pid == "bitwise_and_convolution":
        a, b = rows[1:]
        expected = [0] * len(a)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                expected[i & j] = (expected[i & j] + x * y) % MOD
    elif pid == "kth_term_of_linearly_recurrent_sequence":
        d, k = rows[0]
        a, c = rows[1:]
        # 小さな次数用の独立したKitamasa実装を比較対象にする。
        expected = [lib("math/linear_recurrence")["linear_recurrence"](a, c, k)]
    elif pid == "find_linear_recurrence":
        a = rows[1]
        d = actual[0]
        c = actual[1:]
        assert len(c) == d
        assert all(
            sum(c[j] * a[i - j - 1] for j in range(d)) % MOD == a[i]
            for i in range(d, len(a))
        )
        for k in range(d):
            eq = [[a[i - j - 1] for j in range(k)] for i in range(k, len(a))]
            aug = [row + [a[i]] for i, row in enumerate(eq, k)]
            assert rank(eq, MOD) < rank(aug, MOD)
        return
    elif pid.endswith("_of_formal_power_series"):
        n = rows[0][0]
        a = rows[1]
        if pid.startswith("sqrt"):
            first = next((i for i, x in enumerate(a) if x), n)
            possible = first == n or (
                first % 2 == 0 and pow(a[first], (MOD - 1) // 2, MOD) == 1
            )
            if not possible:
                assert actual == [-1]
            else:
                assert len(actual) == n and mul(actual, actual)[:n] == a
            return
        if pid.startswith("pow"):
            exponent = rows[0][1]
            result = [1] + [0] * (n - 1)
            base = a
            while exponent:
                if exponent & 1:
                    result = (mul(result, base) + [0] * n)[:n]
                base = (mul(base, base) + [0] * n)[:n]
                exponent //= 2
            expected = result
        elif pid.startswith("exp"):
            expected = [1]
            for i in range(1, n):
                expected.append(
                    sum(j * a[j] * expected[i - j] for j in range(1, i + 1))
                    * pow(i, -1, MOD)
                    % MOD
                )
        else:
            inverse = [pow(a[0], -1, MOD)]
            for i in range(1, n):
                inverse.append(
                    -sum(a[j] * inverse[i - j] for j in range(1, i + 1))
                    * inverse[0]
                    % MOD
                )
            if pid.startswith("inv"):
                expected = inverse
            else:
                deriv = mul([i * a[i] % MOD for i in range(1, n)], inverse)
                expected = [0] + [
                    deriv[i - 1] * pow(i, -1, MOD) % MOD for i in range(1, n)
                ]
    else:
        raise AssertionError("missing validator: " + pid)
    assert actual == expected, (pid, actual, expected)


class RoundTwoTests(unittest.TestCase):
    def test_official_samples(self):
        builder = runpy.run_path(str(ROOT / "verify/build.py"))
        problems = [p for p in builder["problems"]() if p not in FIRST]
        self.assertEqual(len(problems), 50)
        count = 0
        for pid in problems:
            source = builder["bundle"](pid)
            self.assertNotIn("from cp_snippet_palette", source)
            target = ROOT / "verify/build" / f"{pid}.py"
            target.parent.mkdir(exist_ok=True)
            target.write_text(source, encoding="utf8")
            for sample in sorted((ROOT / "verify/samples" / pid).glob("*.in")):
                with self.subTest(problem=pid, sample=sample.name):
                    result = subprocess.run(
                        [sys.executable, "-B", "-I", str(target)],
                        input=sample.read_bytes(),
                        capture_output=True,
                        timeout=20,
                    )
                    self.assertEqual(
                        result.returncode, 0, result.stderr.decode(errors="replace")
                    )
                    check_sample(
                        pid, sample.read_text(encoding="utf8"), result.stdout.decode()
                    )
                    count += 1
        self.assertEqual(count, 91)

    def test_versioned_structures_and_deque(self):
        rng = random.Random(201)
        queue = lib("structures/persistent_queue")["PersistentQueue"]()
        versions = [[]]
        for _ in range(160):
            v = rng.randrange(len(versions))
            a = versions[v][:]
            if a and rng.randrange(2):
                new, value = queue.popleft(v)
                self.assertEqual(value, a.pop(0))
            else:
                value = rng.randrange(100)
                new = queue.append(v, value)
                a.append(value)
            self.assertEqual(new, len(versions))
            versions.append(a)
            self.assertEqual(queue.size(v), len(versions[v]))
            if a:
                self.assertEqual(queue.front(new), a[0])
        dsu = lib("structures/rollback_dsu")["RollbackDSU"](5)
        dsu.merge(0, 1)
        mark = dsu.snapshot()
        dsu.merge(1, 2)
        dsu.merge(0, 2)
        dsu.undo()
        self.assertEqual(dsu.size(0), 3)
        dsu.rollback(mark)
        self.assertEqual(dsu.size(0), 2)
        self.assertEqual(dsu.components, 4)
        d = lib("structures/aggregate_deque")["AggregateDeque"](lambda a, b: a + b, "")
        a = deque()
        for _ in range(300):
            t = rng.randrange(4) if a else rng.randrange(2)
            value = chr(97 + rng.randrange(4))
            if t == 0:
                d.append(value)
                a.append(value)
            elif t == 1:
                d.appendleft(value)
                a.appendleft(value)
            elif t == 2:
                self.assertEqual(d.pop(), a.pop())
            else:
                self.assertEqual(d.popleft(), a.popleft())
            self.assertEqual(d.prod(), "".join(a))

    def test_dynamic_sequence(self):
        rng = random.Random(202)
        cls = lib("structures/dynamic_sequence")["DynamicSequence"]
        for mod in (0, 17, MOD):
            a = list(range(12))
            seq = cls(a, mod)
            for _ in range(200):
                t = rng.randrange(5) if a else 0
                l = rng.randrange(len(a) + 1)
                r = rng.randrange(l, len(a) + 1)
                if t == 0:
                    x = rng.randrange(-5, 15)
                    seq.insert(l, x)
                    a.insert(l, x % mod if mod else x)
                elif t == 1:
                    i = rng.randrange(len(a))
                    self.assertEqual(seq.erase(i), a.pop(i))
                elif t == 2:
                    seq.reverse(l, r)
                    a[l:r] = a[l:r][::-1]
                elif t == 3:
                    x, y = rng.randrange(-2, 3), rng.randrange(-5, 6)
                    seq.apply(l, r, x, y)
                    a[l:r] = [(x * v + y) % mod if mod else x * v + y for v in a[l:r]]
                else:
                    self.assertEqual(
                        seq.prod(l, r), sum(a[l:r]) % mod if mod else sum(a[l:r])
                    )
                self.assertEqual(seq.to_list(), a)

    def test_offline_ranges(self):
        rng = random.Random(203)
        points = [(rng.randrange(-4, 5), rng.randrange(-4, 5)) for _ in range(30)]
        bit = lib("structures/fenwick_2d")["OfflineFenwick2D"](points)
        weights = {p: 0 for p in points}
        for _ in range(80):
            x, y = rng.choice(points)
            w = rng.randrange(-8, 9)
            bit.add(x, y, w)
            weights[x, y] += w
            l, r = sorted(rng.sample(range(-6, 7), 2))
            b, t = sorted(rng.sample(range(-6, 7), 2))
            self.assertEqual(
                bit.sum(l, b, r, t),
                sum(w for (x, y), w in weights.items() if l <= x < r and b <= y < t),
            )
        a = [rng.randrange(8) for _ in range(40)]
        queries = [tuple(sorted(rng.sample(range(41), 2))) for _ in range(30)] + [
            (0, 0)
        ]
        self.assertEqual(
            lib("structures/offline_queries")["range_count_distinct"](a, queries),
            [len(set(a[l:r])) for l, r in queries],
        )

    def test_graph_extensions(self):
        rng = random.Random(204)
        matching = lib("graphs/bipartite_matching")["bipartite_matching"]
        for _ in range(80):
            graph = [[v for v in range(6) if rng.randrange(3) == 0] for _ in range(6)]
            left, right = matching(graph, 6)
            self.assertEqual(sum(v != -1 for v in left), matching_size(graph))
            self.assertTrue(
                all(
                    v == -1 or (v in graph[u] and right[v] == u)
                    for u, v in enumerate(left)
                )
            )
        graph = [[] for _ in range(30)]
        for v in range(1, 30):
            p = rng.randrange(v)
            graph[v].append(p)
            graph[p].append(v)
        hld = lib("graphs/hld")["HLD"](30, graph)
        for _ in range(50):
            u, v = rng.randrange(30), rng.randrange(30)
            path = path_between(graph, u, v)
            self.assertEqual(
                [hld.jump(u, v, k) for k in range(len(path) + 1)], path + [-1]
            )
        for directed in (True, False):
            for _ in range(12):
                edges = [(rng.randrange(6), rng.randrange(6)) for _ in range(7)]
                result = lib("graphs/cycle")["find_cycle"](6, edges, directed)
                pid = "cycle_detection" if directed else "cycle_detection_undirected"
                if result is None:
                    output = "-1"
                else:
                    vertices, ids = result
                    output = " ".join(
                        map(str, [len(ids)] + ([] if directed else vertices) + ids)
                    )
                check_sample(
                    pid, "6 7\n" + "\n".join(f"{u} {v}" for u, v in edges), output
                )

    def test_math_and_strings(self):
        rng = random.Random(205)
        poly = lib("math/polynomial")
        gf = lib("math/gf2_matrix")
        for _ in range(20):
            a = [rng.randrange(MOD) for _ in range(8)]
            b = [rng.randrange(MOD) for _ in range(5)]
            self.assertEqual(poly["polynomial_divmod"](a, b), divmod_naive(a, b))
            c = [rng.randrange(5) for _ in range(4)]
            initial = a[:4]
            self.assertEqual(
                poly["linear_recurrence_ntt"](initial, c, 70),
                lib("math/linear_recurrence")["linear_recurrence"](initial, c, 70),
            )
            inverse = poly["polynomial_inverse"](a, b)
            if inverse is not None:
                self.assertEqual(divmod_naive(mul(a, inverse), b)[1], [1])
            rows = [rng.randrange(32) for _ in range(5)]
            matrix = [[(x >> j) & 1 for j in range(5)] for x in rows]
            self.assertEqual(gf["matrix_rank_gf2"](rows, 5), rank(matrix, 2))
            inv = gf["inverse_matrix_gf2"](rows)
            if inv is None:
                self.assertLess(rank(matrix, 2), 5)
            else:
                self.assertEqual(
                    gf["matrix_product_gf2"](rows, inv, 5), [1 << i for i in range(5)]
                )
            a = [rng.randrange(100) for _ in range(8)]
            b = [rng.randrange(100) for _ in range(8)]
            expected = [
                sum(a[i] * b[j] for i in range(8) for j in range(8) if i & j == k) % MOD
                for k in range(8)
            ]
            self.assertEqual(
                lib("math/bit_transforms")["and_convolution"](a, b), expected
            )
            s, t = ("".join(rng.choice("abc") for _ in range(10)) for _ in range(2))
            answer = lib("strings/suffix_array")["longest_common_substring"](s, t)
            check_sample(
                "longest_common_substring", s + "\n" + t, " ".join(map(str, answer))
            )
        self.assertEqual(poly["polynomial_inverse"]([1], [7]), [])


if __name__ == "__main__":
    unittest.main()
