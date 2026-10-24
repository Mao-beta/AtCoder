"""Extracted libraries: standalone loading, representative cases, bug regressions.
Run from cp_snippet_palette: python -B -m unittest discover -s tests -v
"""

from pathlib import Path
import math
import random
import runpy
import unittest

ROOT = Path(__file__).absolute().parents[1] / "library"


def lib(name):
    return runpy.run_path(str(ROOT / (name + ".py")))


class LibraryTests(unittest.TestCase):
    def test_standalone_modules(self):
        for path in ROOT.rglob("*.py"):
            with self.subTest(module=path.stem):
                runpy.run_path(str(path))

    def test_acl_structure_interfaces(self):
        folder = ROOT.parent / "snippets" / "structures"

        def snippet(name):
            return runpy.run_path(str(folder / (name + ".py")))

        m = snippet("UnionFind")
        uf = m["dsu"](4)
        self.assertEqual(uf.merge(1, 2), uf.leader(2))
        self.assertTrue(uf.same(1, 2))
        self.assertEqual(uf.size(1), 2)
        self.assertEqual(sorted(map(sorted, uf.groups())), [[0], [1, 2], [3]])
        self.assertEqual(m["dsu"](0).groups(), [])
        uf = snippet("WeightedUnionFind")["WeightedUnionFind"](4)
        self.assertEqual(uf.merge(a=1, b=2, w=5), 1)
        self.assertEqual(uf.merge(0, 2, 8), 1)
        self.assertEqual(uf.merge(1, 2, 5), 1)
        self.assertEqual((uf.diff(0, 1), uf.potential(2)), (3, 5))
        self.assertEqual(uf.groups(), [[0, 1, 2], [3]])
        self.assertTrue(uf.same(0, 2))
        with self.assertRaises(ValueError):
            uf.merge(0, 2, 9)
        with self.assertRaises(ValueError):
            uf.diff(0, 3)
        fw = snippet("BIT")["fenwick_tree"](3)
        for i, x in enumerate([2, 5, 3]):
            fw.add(i, x)
        self.assertEqual(fw.sum(1, 3), 8)
        self.assertEqual(fw.sum(2, 2), 0)
        self.assertEqual(fw.sum0(2), 7)
        self.assertEqual(fw.lower_bound(8), 2)
        self.assertNotIn("BIT", snippet("BIT"))
        seg = snippet("segtree")["segtree"](
            V=["a", "b", "c"], OP=lambda x, y: x + y, E=""
        )
        seg.set(1, "xy")
        self.assertEqual(seg.prod(0, 3), "axyc")
        self.assertEqual(seg.max_right(0, lambda x: len(x) <= 3), 2)
        self.assertEqual(seg.min_left(3, lambda x: len(x) <= 3), 1)
        self.assertEqual(snippet("segtree")["segtree"]([], max, -1).all_prod(), -1)
        op = lambda x, y: (x[0] + y[0], x[1] + y[1])
        mapping = lambda f, x: (f[0] * x[0] + f[1] * x[1], x[1])
        composition = lambda f, g: (f[0] * g[0], f[0] * g[1] + f[1])
        lazy = snippet("lazy_segtree")["lazy_segtree"](
            OP=op,
            E=(0, 0),
            MAPPING=mapping,
            COMPOSITION=composition,
            ID=(1, 0),
            V=[(1, 1), (2, 1), (3, 1)],
        )
        lazy.apply(0, 3, (2, 1))
        lazy.apply(0, 2, (3, 4))
        lazy.apply_point(1, (0, 9))
        self.assertEqual(lazy.to_list(), [(13, 1), (9, 1), (7, 1)])
        self.assertEqual(lazy.prod(0, 3), (29, 3))
        self.assertEqual(lazy.max_right(0, lambda x: x[0] <= 22), 2)
        self.assertEqual(lazy.min_left(3, lambda x: x[0] <= 16), 1)

    def test_sequence(self):
        m = lib("basic/sequence")
        self.assertEqual(m["compress"]([8, -2, 8]), ([1, 0, 1], [-2, 8]))
        a = [-(10**90), 3, 3, 2, 10**90]
        self.assertEqual(m["lis_length"](a), 3)
        self.assertEqual(m["lis_length"](a, False), 4)
        self.assertEqual(len(m["lis_indices"](a)), 3)
        self.assertEqual(m["inversion_count"]([3, 1, 1, 2]), 3)
        self.assertEqual(
            m["run_length_decode"](m["run_length_encode"]("aaabb")), list("aaabb")
        )
        self.assertEqual(m["lis_indices"]([]), [])

    def test_prefix_sum(self):
        m = lib("basic/prefix_sum_2d")
        p = m["prefix_sum_2d"]([[1, -2, 3], [4, 5, 6]])
        self.assertEqual(m["rectangle_sum"](p, 0, 1, 2, 3), 12)
        self.assertEqual(m["rectangle_sum"](p, 1, 2, 1, 3), 0)
        self.assertEqual(m["prefix_sum_2d"]([]), [[0]])

    def test_doubling(self):
        d = lib("basic/doubling")["Doubling"]([1, 2, -1], 8)
        self.assertEqual([d.jump(0, k) for k in range(5)], [0, 1, 2, -1, -1])
        with self.assertRaises(ValueError):
            d.jump(0, 9)

    def test_lca_zero_indexed(self):
        Tree = runpy.run_path(str(ROOT.parent / "snippets/structures/LCATree.py"))["LCATree"]
        edges = [(0, 1), (0, 2), (2, 3), (2, 4)]
        tree = Tree(5, edges)
        self.assertEqual(tree.root, 0)
        self.assertEqual(tree.parent[0], [-1, 0, 0, 2, 2])
        self.assertEqual(tree.depth, [0, 1, 1, 2, 2])
        self.assertEqual((tree.lca(0, 4), tree.lca(3, 4)), (0, 2))
        self.assertEqual(tree.get_path(1, 4), [1, 0, 2, 4])
        self.assertEqual(tree.distance(1, 4), 3)
        self.assertEqual([tree.jump(1, 4, k) for k in range(5)], [1, 0, 2, 4, -1])
        self.assertEqual([tree.kth_ancestor(4, k) for k in range(4)], [4, 2, 0, -1])
        self.assertTrue(tree.is_ancestor(0, 0))
        self.assertFalse(tree.is_ancestor(1, 4))
        self.assertEqual((tree.subtree_size(0), tree.subtree_size(2)), (5, 3))
        self.assertEqual(Tree(5, edges, root=4).lca(1, 3), 2)
        single = Tree(1, [])
        self.assertEqual((single.lca(0, 0), single.jump(0, 0, 1)), (0, -1))
        for n, bad_edges, root in [(0, [], 0), (1, [], 1), (2, [(0, 2)], 0),
                                   (3, [(0, 1)], 0), (3, [(0, 1), (1, 2), (2, 0)], 0)]:
            with self.assertRaises(ValueError):
                Tree(n, bad_edges, root)
        for vertex in (-1, 5):
            with self.assertRaises(AssertionError):
                tree.lca(vertex, 0)

    def test_grid(self):
        m = lib("basic/grid")
        self.assertEqual(
            m["rotate90"]([[1, 2, 3], [4, 5, 6]]), [[4, 1], [5, 2], [6, 3]]
        )
        self.assertEqual(m["to_position"](m["to_index"](2, 3, 5), 5), (2, 3))
        self.assertFalse(m["in_grid"](2, 0, 2, 3))

    def test_sliding(self):
        m = lib("basic/sliding_window")
        self.assertEqual(m["sliding_min"]([3, 1, 4, 1, 5], 3), [1, 1, 1])
        self.assertEqual(m["area_min_sliding"]([[3, 2], [1, 4]], 2, 1), [[1, 2]])
        self.assertEqual(m["largest_rectangle_in_histogram"]([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(m["largest_rectangle_in_grid"]([[1, 1, 0], [1, 1, 1]]), 4)

    def test_subset_dp(self):
        m = lib("basic/subset_dp")
        self.assertEqual(m["split_and_list"]([1, 2, 3]), ([0, 1], [0, 2, 3, 5]))
        self.assertEqual(sorted(m["subset_sums_by_size"]([1, 2, 3])[2]), [3, 4, 5])
        self.assertEqual(m["knapsack_01"]([(0, 3), (2, 4), (3, 5)], 3), 8)
        self.assertEqual(m["subset_sum_bits"]([2, 3], 5), 0b101101)

    def test_matrix(self):
        m = lib("basic/matrix")
        self.assertEqual(
            m["matrix_power"]([[1, 1], [1, 0]], 10, 1000000007), [[89, 55], [55, 34]]
        )
        self.assertEqual(m["matrix_power"]([[5]], 0, 1), [[0]])
        inf = -(1 << 60)
        self.assertEqual(m["max_plus_power"]([[0, 2], [inf, 0]], 2), [[0, 2], [inf, 0]])

    def test_shortest_paths(self):
        m = lib("graphs/shortest_paths")
        g = m["weighted_adjlist"](4, [(0, 1, 1), (1, 2, 0), (0, 2, 1)], True)
        d, p = m["dijkstra"](g, 0)
        self.assertEqual(d, m["zero_one_bfs"](g, 0))
        self.assertEqual(d[:3], [0, 1, 1])
        self.assertEqual(m["restore_path"](p, 0, 3), [])
        self.assertEqual(
            m["floyd_warshall"](3, [(0, 1, 5), (0, 1, 2), (1, 2, -1)])[0][2], 1
        )
        _, negative = m["bellman_ford"](4, [(0, 1, 0), (1, 1, -1), (1, 2, 0)], 0)
        self.assertEqual(negative, [False, True, True, False])
        self.assertEqual(m["topological_sort"]([[1], [2], []]), [0, 1, 2])
        with self.assertRaises(ValueError):
            m["topological_sort"]([[0]])

    def test_scc_two_sat(self):
        m = lib("graphs/scc")
        edges = [(0, 1), (1, 0), (1, 2), (2, 3)]
        ids = m["scc_ids"](4, edges)
        self.assertEqual(ids[0], ids[1])
        self.assertLess(ids[1], ids[2])
        self.assertEqual(m["scc"](4, edges), [[0, 1], [2], [3]])
        clause = [(0, True, 0, True), (0, False, 1, True)]
        self.assertEqual(m["two_sat"](2, clause), [True, True])
        self.assertIsNone(m["two_sat"](2, clause + [(1, False, 1, False)]))
        self.assertEqual(m["two_sat"](0, []), [])

    def test_lowlink(self):
        c = lib("graphs/lowlink")["LowLink"]
        g = c(5, [(0, 1), (0, 1), (1, 2), (3, 4), (2, 2)])
        self.assertEqual(set(g.bridges), {2, 3})
        self.assertEqual(g.articulation, {1})
        self.assertEqual(c(3, [(0, 1), (1, 2), (2, 0)]).bridges, [])

    def test_rerooting(self):
        m = lib("graphs/rerooting")
        graph = [[1], [0, 2], [1]]
        self.assertEqual(
            m["rerooting"](graph, lambda a, b: a + b, 0, lambda value, u, v: value + 1),
            [2, 2, 2],
        )
        self.assertEqual(
            m["rerooting"](graph, max, 0, lambda value, u, v: value + 1), [2, 1, 2]
        )

    def test_tree_and_hld(self):
        graph = [[1], [0, 2, 3], [1], [1]]
        m = lib("graphs/tree")
        order, tin, tout, parent = m["euler_tour"](graph)
        self.assertEqual(set(order[tin[1] : tout[1]]), {1, 2, 3})
        self.assertEqual(m["tree_diameter"](graph)[0], 2)
        self.assertEqual(m["tree_centers"](graph), [1])
        self.assertEqual(
            m["postorder_from_preorder_inorder"]([1, 2, 3], [2, 1, 3]), [2, 3, 1]
        )
        m = lib("graphs/hld")
        h = m["HLD"](4, graph)
        values = [""] * 4
        for i, ch in enumerate("abcd"):
            values[h.pos[i]] = ch
        seg = m["BiSegTree"](values, lambda a, b: a + b, "")
        self.assertEqual(m["path_prod"](h, seg, 2, 3), "cbd")
        self.assertEqual(m["path_prod"](h, seg, 3, 0), "dba")
        self.assertEqual(m["path_prod"](h, seg, 2, 3, edge=True), "cd")

    def test_centroid(self):
        c = lib("graphs/centroid_decomposition")["CentroidDecomposition"]
        self.assertEqual(c(0, []).cd_parents, [])
        p = c(5, [[1], [0, 2], [1, 3], [2, 4], [3]]).cd_parents
        self.assertEqual(p[2], -1)
        self.assertEqual(p.count(-1), 1)

    def test_flow_and_mst(self):
        mf = lib("graphs/max_flow")["mf_graph"](4)
        for u, v, capacity in [(0, 1, 3), (0, 2, 2), (1, 2, 1), (1, 3, 2), (2, 3, 3)]:
            mf.add_edge(u, v, capacity)
        self.assertEqual(mf.flow(0, 3), 5)
        self.assertEqual(mf.get_edge(0).From, 0)
        self.assertEqual(mf.get_edge(0).Flow, 3)
        self.assertEqual(mf.edges()[0], {"from": 0, "to": 1, "cap": 3, "flow": 3})
        self.assertEqual(mf.edges(False)[0].To, 1)
        self.assertEqual(mf.min_cut(0), [True, False, False, False])
        mc = lib("graphs/min_cost_flow")["mcf_graph"](3)
        self.assertIsNone(mc.add_edge(0, 1, 2, 3))
        mc.add_edge(1, 2, 2, 4)
        mc.add_edge(0, 2, 1, 10)
        self.assertEqual(mc.flow(0, 2, 3), (3, 24))
        self.assertEqual(
            mc.get_edge(0), {"from": 0, "to": 1, "cap": 2, "flow": 2, "cost": 3}
        )
        with self.assertRaises(ValueError):
            mc.flow(0, 2)
        m = lib("graphs/mst")
        self.assertEqual(
            m["minimum_spanning_forest"](4, [(0, 1, 3), (1, 2, 1), (0, 2, 2)])[::2],
            (3, 2),
        )

    def test_matching_and_exponential(self):
        match = lib("graphs/bipartite_matching")["bipartite_matching"]([[0, 1], [0]], 2)
        self.assertEqual(match, ([1, 0], [1, 0]))
        m = lib("graphs/exponential")
        distance = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]
        self.assertEqual(m["tsp_cycle"](distance), 9)
        self.assertEqual(
            m["steiner_tree"](
                4, [(0, 1, 2), (1, 2, 3), (1, 3, 1), (0, 1, 8)], [0, 2, 3]
            ),
            6,
        )
        self.assertEqual(m["chinese_postman"](3, [(0, 1, 2), (1, 2, 3)]), 10)
        self.assertEqual(m["chinese_postman"](4, [(0, 1, 1), (2, 3, 1)]), 1 << 60)
        triangle = [[1, 2], [0, 2], [0, 1]]
        self.assertEqual(len(m["maximum_independent_set"](triangle)), 1)
        self.assertEqual(m["chromatic_number"](triangle), 3)
        self.assertEqual(m["chromatic_number"]([[1], [0, 2], [1]]), 2)
        self.assertEqual(m["chromatic_number"]([]), 0)

    def test_strings(self):
        m = lib("strings/matching")
        self.assertEqual(m["kmp_search"]("aaaa", "aa"), [0, 1, 2])
        self.assertEqual(m["kmp_search"]("ab", ""), [0, 1, 2])
        self.assertEqual(m["manacher"]("abba"), ([1, 1, 1, 1], [0, 0, 2, 0]))
        self.assertEqual(m["edit_distance"]("kitten", "sitting"), 3)
        self.assertEqual(m["lcs_length"]("abcbdab", "bdcaba"), 4)
        m = lib("strings/suffix_array")
        self.assertEqual(m["String"]([2, 0, 2, 0]).suffix_array(), [3, 1, 2, 0])
        for value in ["banana", "漢字漢", [5, 2, 3, 2, -1], [], [2, 2, 1, 1, 0]]:
            sa = m["String"](value).suffix_array()
            self.assertEqual(sa, sorted(range(len(value)), key=lambda i: value[i:]))
        self.assertEqual(
            m["String"]("banana").lcp_array([5, 3, 1, 0, 4, 2]), [1, 3, 0, 0, 2]
        )
        self.assertEqual(m["String"]("aaaa").z_algorithm(), [4, 3, 2, 1])

    def test_trie_and_hash(self):
        m = lib("strings/trie")
        t = m["Trie"]()
        for s in ["ab", "ab", "ac", ""]:
            t.add(s)
        self.assertEqual((t.count("ab"), t.count_prefix("a")), (2, 3))
        a = m["AhoCorasick"](["he", "she", "hers", "he", ""])
        self.assertEqual(a.count("ushers"), [1, 1, 1, 1, 7])
        m = lib("strings/rolling_hash")
        h, t = m["RollingHash"]("abcabc"), m["RollingHashSegTree"]("abcabc")
        self.assertEqual(h.query(0, 3), h.query(3, 6))
        self.assertEqual(t.query(1, 5), h.query(1, 5))
        t.set(1, "x")
        self.assertEqual(t.query(0, 6), m["RollingHash"]("axcabc").query(0, 6))

    def test_sorted_and_avl(self):
        m = lib("structures/sorted_set")
        s = m["SortedMultiset"]([3, 1, 3])
        self.assertEqual(list(s), [1, 3, 3])
        self.assertTrue(s.discard(3))
        self.assertFalse(s.discard(8))
        self.assertEqual((s.bisect_left(3), s.bisect_right(3)), (1, 2))
        self.assertEqual(list(m["SortedSet"]([3, 1, 3])), [1, 3])
        tree = lib("structures/avl_tree")["AVLTree"]()
        rng = random.Random(42)
        keys = list(range(35))
        rng.shuffle(keys)
        for k in keys:
            tree[k] = k * 2
        for k in keys[:20]:
            del tree[k]
        remaining = sorted(keys[20:])
        self.assertEqual([tree.kth(i) for i in range(len(tree))], remaining)
        self.assertEqual([tree[k] for k in remaining], [2 * k for k in remaining])
        self.assertEqual(tree.get(99, "missing"), "missing")
        self.assertFalse(tree.discard(99))
        with self.assertRaises(KeyError):
            _ = tree[99]
        with self.assertRaises(KeyError):
            del tree[99]
        with self.assertRaises(IndexError):
            tree.kth(len(tree))
        for key in (0, 17, 35):
            self.assertEqual(tree.ge(key), next((x for x in remaining if x >= key), None))
            self.assertEqual(tree.lt(key), next((x for x in reversed(remaining) if x < key), None))

    def test_binary_and_wavelet(self):
        t = lib("structures/binary_trie")["BinaryTrie"](5)
        for x in [4, 1, 4, 7]:
            t.add(x)
        self.assertEqual([t.kth(i) for i in range(len(t))], [1, 4, 4, 7])
        self.assertEqual(t.min_xor(6), 1)
        self.assertEqual(t.count_less(4), 1)
        t.discard(4)
        self.assertEqual(t.count(4), 1)
        m = lib("structures/wavelet_matrix")
        bits = m["FullyIndexableDictionary"](64)
        bits.set(31, 1)
        bits.set(32, 1)
        bits.set(31, 0)
        bits.build()
        self.assertEqual(bits.rank(64, 1), 1)
        self.assertEqual([bits.select(1, k) for k in (-1, 0, 1)], [-1, 32, -1])
        self.assertEqual([bits.select(0, k) for k in (0, 31, 32, 62, 63)], [0, 31, 33, 63, -1])
        self.assertIsNone(m["FullyIndexableDictionary"](0).select(0, 0, None))
        a = [-3, 8, -3, 1]
        w = m["WaveletMatrix"](a)
        self.assertEqual([w[i] for i in range(4)], a)
        self.assertEqual([w.kth_smallest(0, 4, k) for k in range(4)], sorted(a))
        self.assertEqual(w.count_less(1, 4, 2), 2)
        self.assertEqual([w.select(-3, k) for k in (-1, 0, 1, 2)], [-1, 0, 2, -1])
        self.assertEqual(w.select(8, 0, default=0), 1)
        self.assertEqual(w.sum(2, 2), 0)
        for values in ([], [0], [-3, 8, -3, 1], [5, 5]):
            w = m["WaveletMatrix"](values)
            for bad in (-len(values) - 1, len(values)):
                with self.assertRaises(IndexError):
                    w.get(bad)
            for l in range(len(values) + 1):
                for r in range(l, len(values) + 1):
                    ordered = sorted(values[l:r])
                    for method in (w.kth_smallest, w.kth_largest):
                        expected = ordered[::-1] if method == w.kth_largest else ordered
                        self.assertEqual([method(l, r, k) for k in range(r - l)], expected)
                        for k in (-1, r - l):
                            with self.assertRaises(IndexError):
                                method(l, r, k)
            for value in set(values) | {99}:
                positions = [i for i, x in enumerate(values) if x == value]
                self.assertEqual([w.select(value, k) for k in range(len(positions))], positions)
                self.assertIsNone(w.select(value, len(positions), default=None))

    def test_mo(self):
        m = lib("structures/mo")
        values = [2, 3, 5, 7]
        state = [0]

        def add(i):
            state[0] += values[i]

        def remove(i):
            state[0] -= values[i]

        self.assertEqual(
            m["mo_solve"](
                4, [(2, 4), (0, 1), (0, 0), (0, 4)], add, remove, lambda: state[0]
            ),
            [12, 2, 0, 17],
        )

    def test_priority_sum_and_max_queue(self):
        t = lib("structures/priority_sum")["PrioritySumStructure"](0)
        a = [4, 1, 1, 7]
        for x in a:
            t.add(x)
        self.assertEqual(t.query(), 0)
        t.set_k(3)
        self.assertEqual(t.query(), 6)
        self.assertTrue(t.discard(1))
        self.assertFalse(t.discard(99))
        self.assertEqual(t.query(), 12)
        q = lib("structures/max_queue")["MaxQueue"]()
        q.set("a", 5)
        q.discard("a")
        q.set("a", 8)
        q.set("b", 6)
        self.assertEqual(q.pop(), ("a", 8))
        self.assertEqual(q.top(), ("b", 6))

    def test_slope_and_li_chao(self):
        t = lib("structures/slope_trick")["SlopeTrick"]()
        for x in [1, 4, 9]:
            t.add_abs(x)
        self.assertEqual(t.minimum, 8)
        self.assertEqual(t.argmin(), (4, 4))
        for x in range(-2, 12):
            self.assertEqual(t.evaluate(x), sum(abs(x - a) for a in [1, 4, 9]))
        t.shift(2, 2)
        self.assertEqual(t.argmin(), (6, 6))
        cls = lib("structures/li_chao")["LiChaoInt"]
        for mode in ["min", "max"]:
            lc = cls(-10, 11, mode)
            self.assertIsNone(lc.query(-10))
            with self.assertRaises(ValueError):
                lc.query(11)
            lines = [(2, 5), (-3, 2), (0, 10**90)]
            for a, b in lines:
                lc.add_line(a, b)
            for x in [-10, -1, 0, 7, 10]:
                self.assertEqual(
                    lc.query(x),
                    (min if mode == "min" else max)(a * x + b for a, b in lines),
                )

    def test_dynamic_fenwick(self):
        m = lib("structures/dynamic_fenwick")
        b = m["DynamicFenwickTree"](100)
        b.add(2, 4)
        b.add(90, 5)
        self.assertEqual(b.sum(0, 91), 9)
        self.assertEqual(b.sum0(r=91), 9)
        self.assertEqual(b.lower_bound(5), 90)
        self.assertEqual(b.lower_bound(10), 100)
        b = m["DynamicFenwickTree2D"](10**9, 10**9)
        b.add(2, 3, 7)
        b.add(5, 6, -2)
        self.assertEqual(b.sum(0, 0, 6, 7), 5)
        self.assertEqual(b.sum0(6, 7), 5)
        with self.assertRaises(IndexError):
            b.add(-1, 2, 1)

    def test_arithmetic_and_sqrt(self):
        Beats = runpy.run_path(str(ROOT.parent / "snippets/structures/SegmentTreeBeats.py"))["SegmentTreeBeats"]
        beats = Beats(V=[1, 5, 3, 7])
        beats.chmin(l=0, r=4, x=4)
        beats.chmax(0, 2, 2)
        beats.add(1, 3, 10)
        self.assertEqual(beats.prod(0, 4), (2, 14, 33))
        beats.assign(2, 4, 0)
        beats.set(0, -1)
        self.assertEqual(beats.to_list(), [-1, 14, 0, 0])
        self.assertEqual((beats.min(0, 4), beats.max(0, 4), beats.sum(0, 4)), (-1, 14, 13))
        self.assertEqual(Beats([]).prod(0, 0), (math.inf, -math.inf, 0))
        a = [2, -1, 5, 4, 7, 3, 0]
        t = lib("structures/range_arithmetic")["ArithmeticSegmentTree"](a)
        t.add(1, 6, 2, -1)
        for i in range(1, 6):
            a[i] += 2 - (i - 1)
        t.assign(2, 5, 7, 3)
        for i in range(2, 5):
            a[i] = 7 + 3 * (i - 2)
        t.add(0, 7, -2)
        a = [x - 2 for x in a]
        for l, r in [(0, 7), (2, 6), (3, 3), (1, 2)]:
            self.assertEqual(t.sum(l, r), sum(a[l:r]))
        b = lib("structures/sqrt_decomposition")["SqrtDecomposition"](a)
        b.add(1, 6, 4)
        for i in range(1, 6):
            a[i] += 4
        self.assertEqual(b.sum(2, 7), sum(a[2:7]))

    def test_small_structures(self):
        Heap = runpy.run_path(str(ROOT.parent / "snippets/structures/Heapq.py"))["Heapq"]
        heap = Heap([3, 1, 3])
        self.assertTrue(heap.discard(3))
        self.assertFalse(heap.discard(9))
        self.assertEqual((heap.top(), heap.pop(), heap.pop()), (1, 1, 3))
        for method in (heap.top, heap.pop):
            with self.assertRaises(IndexError):
                method()
        c = lib("structures/cartesian_tree")["CartesianTree"]([3, 1, 1, 2])
        self.assertEqual((c.root, c.parent), (1, [1, -1, 1, 2]))
        linked = lib("structures/linked_list")["LinkedList"]()
        i = linked.append(3)
        self.assertEqual(i, 0)
        front = linked.insert_after(-1, 2)
        back = linked.insert_after(i, 4)
        self.assertEqual((front, back), (1, 2))
        self.assertEqual(list(linked), [2, 3, 4])
        linked.erase(i)
        self.assertEqual(list(linked), [2, 4])
        linked.erase(front)
        linked.erase(back)
        self.assertEqual((len(linked), list(linked), linked.head, linked.tail), (0, [], -1, -1))
        self.assertEqual(linked.append(7), 3)
        self.assertEqual(list(linked), [7])
        for node in (-2, -1, 0, 4):
            with self.assertRaises(IndexError):
                linked.erase(node)
        for node in (-2, 0, 4):
            with self.assertRaises(IndexError):
                linked.insert_after(node, 8)
        b = lib("structures/bit_set")["BitSet"](130)
        b.set(129)
        b.set(5)
        b.set(5, False)
        self.assertEqual(list(b.indices()), [129])
        self.assertEqual(b.shifted(1).count(), 0)

    def test_number_theory(self):
        m = lib("math/number_theory")
        self.assertEqual(m["pow_mod"](-2, 5, 7), 3)
        self.assertEqual(m["pow_mod"](0, 0, 1), 0)
        self.assertEqual(m["crt"]([2, 3], [6, 9]), (0, 0))
        self.assertEqual(m["crt"]([2, 5], [6, 9]), (14, 18))
        self.assertEqual(m["inv_mod"](3, 8), 3)
        self.assertEqual(
            m["floor_sum"](8, 7, -3, -5), sum((-3 * i - 5) // 7 for i in range(8))
        )
        for a, b, mod, answer in [
            (2, 4, 8, 2),
            (2, 0, 8, 3),
            (3, 1, 7, 0),
            (0, 0, 5, 1),
            (2, 3, 8, -1),
        ]:
            self.assertEqual(m["discrete_log"](a, b, mod), answer)
        self.assertEqual(m["sqrt_mod"](10, 13), 6)
        self.assertEqual(m["sqrt_mod"](2, 13), -1)

    def test_combinatorics_and_factorization(self):
        m = lib("math/combinatorics")
        c = m["Comb"](20, 101)
        for n, k in [(0, 0), (5, 2), (15, 7), (20, 20)]:
            self.assertEqual(c.combination(n, k), math.comb(n, k) % 101)
        self.assertEqual(c.homogeneous(0, 0), 1)
        self.assertEqual(
            m["combination_small_k"](10**9, 2), math.comb(10**9, 2) % 998244353
        )
        self.assertEqual(m["primes_up_to"](10), [2, 3, 5, 7])
        self.assertEqual(m["factorize_trial"](72), {2: 3, 3: 2})
        self.assertEqual(m["divisors"](12), [1, 2, 3, 4, 6, 12])
        f = lib("math/factorize64")
        self.assertFalse(f["is_probable_prime"](-3))
        self.assertEqual(sorted(f["divisors"](12)), [1, 2, 3, 4, 6, 12])
        self.assertEqual(f["totient"](12), 4)
        self.assertEqual(f["lcm"](6, 8), 24)
        self.assertFalse(f["is_probable_prime"](341550071728321))
        self.assertEqual(f["prime_fact"](1000003 * 1000033), {1000003: 1, 1000033: 1})

    def test_bit_transforms_and_scalar(self):
        m = lib("math/bit_transforms")
        a = [2, 4, 6, 8]
        self.assertEqual(m["subset_zeta"](m["subset_zeta"](a), True), a)
        self.assertEqual(m["subset_zeta"]([8], mod=3), [2])
        self.assertEqual(m["xor_maximum"](m["xor_basis"]([3, 5])), 6)
        self.assertEqual(
            m["xor_minimax"]([0, 2, 5]),
            min(max(x ^ v for v in [0, 2, 5]) for x in range(8)),
        )
        self.assertEqual(m["solve_gf2"]([0b11, 0b10], [1, 0], 2), (2, 1))
        self.assertIsNone(m["solve_gf2"]([1, 1], [0, 1], 1))
        m = lib("math/scalar")
        with m["ModContext"](11):
            a, b = m["Modint"](10), m["Modint"](3)
            self.assertEqual((a / b).val(), 7)
            self.assertEqual(b.inv().val(), 4)
            self.assertEqual((b ** 4).val(), 4)
            self.assertEqual(m["raw"](3).mod(), 11)
            with m["ModContext"](7):
                self.assertEqual(m["Modint"](10).val(), 3)
            self.assertEqual(m["Modint"](10).val(), 10)
        with m["ModContext"](8):
            c = m["Modint"](3)
        self.assertEqual(int(5 / c), 7)
        self.assertEqual(m["Fraction"](2, 4), m["Fraction"](1, 2))

    def test_recurrence(self):
        m = lib("math/linear_recurrence")
        self.assertEqual(m["berlekamp_massey"]([0, 1, 1, 2, 3, 5, 8, 13]), [1, 1])
        self.assertEqual(m["linear_recurrence"]([0, 1], [1, 1], 20), 6765)

    def test_polynomial(self):
        m = lib("math/polynomial")
        self.assertEqual(m["FFT"](998244353).convolution([1, 2], [3, 4]), [3, 10, 8])
        with self.assertRaises(ValueError):
            m["FFT"](1000000007).convolution([1] * 41, [1] * 41)
        mod = m["FPS_MOD"]
        a = list(range(65))
        b = [i * i - 100 for i in range(70)]
        expected = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                expected[i + j] = (expected[i + j] + x * y) % mod
        self.assertEqual(m["FFT"](998244353).convolution(a, b), expected)
        self.assertEqual(m["fps_inverse"]([1, -1], 6), [1] * 6)
        self.assertEqual(
            m["fps_exp"](m["fps_log"]([1, 2, 3], 8), 8), [1, 2, 3, 0, 0, 0, 0, 0]
        )
        self.assertEqual(m["fps_power"]([0], 0, 4), [1, 0, 0, 0])
        self.assertEqual(m["fps_power"]([0, 1], 3, 5), [0, 0, 0, 1, 0])
        root = m["fps_sqrt"]([1, 2, 1], 5)
        self.assertEqual(
            m["FFT"](998244353).convolution(root, root)[:5], [1, 2, 1, 0, 0]
        )
        self.assertEqual(m["polynomial_gcd"]([-1, 0, 1], [-1, 1]), [mod - 1, 1])
        self.assertEqual(m["polynomial_gcd"]([], []), [])
        self.assertEqual(m["bostan_mori"]([0, 2], [2, -2, -2], 10), 55)
        self.assertEqual(m["subset_sum"]([0, 1, 1, 8], 3), [2, 4, 2, 0])
        self.assertEqual(m["partition_function"](5), [1, 1, 2, 3, 5, 7])
        self.assertEqual(m["stirling_second"](4), [0, 1, 7, 6, 1])
        self.assertEqual(m["stirling_first"](4), [0, mod - 6, 11, mod - 6, 1])
        self.assertEqual(
            m["polynomial_interpolation"]([0, 1, 2], [1, 6, 17]).Func, [1, 2, 3]
        )
        inv = m["polynomial_inverse"]([1, 1], [1, 0, 1])
        F = m["FPS"]
        self.assertEqual(F([1, -1]).inv(d=5).Func, [1] * 5)
        self.assertEqual(F([1, 2, 1]).log(5).exp(5).Func, [1, 2, 1, 0, 0])
        self.assertEqual(F([1, 1]).powfps(3, 4).Func, [1, 3, 3, 1])
        self.assertEqual(F([1, 2, 1]).sqrt(3).Func, [1, 1, 0])
        self.assertEqual(F([0, 1]).sqrt(3).Func, [])
        self.assertEqual(F([1, 2, 3]).diff().integral().Func, [0, 2, 3])
        result = F(m["FFT"](998244353).convolution([1, 1], inv)) % F([1, 0, 1])
        result.reduce()
        self.assertEqual(result.Func, [1])
        common = [3, 2, 1]
        f = m["FFT"](998244353).convolution(common, [0] * 70 + [1])
        g = m["FFT"](998244353).convolution(common, [1] + [0] * 69 + [1])
        self.assertEqual(m["polynomial_gcd"](f, g), common)

    def test_geometry(self):
        m = lib("geometry/convex")
        points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 0), (0, 0)]
        hull = m["convex_hull_points"](points)
        self.assertEqual(m["convex_diameter_sq"](hull), 8)
        polygon = m["ConvexPolygon"](points)
        self.assertEqual(
            [polygon.locate(p) for p in [(1, 1), (1, 0), (3, 1)]], [1, 0, -1]
        )
        self.assertIs(polygon.contains((1, 0)), True)
        self.assertIs(polygon.contains_strict((1, 0)), False)
        self.assertEqual(m["ConvexPolygon"]([]).locate((0, 0)), -1)
        self.assertEqual(m["ConvexPolygon"]([(0, 0)]).locate((0, 0)), 0)
        for filename in ("02_line_segment", "03_polygon_convex", "05_circle"):
            geom = runpy.run_path(str(ROOT.parent / "snippets/geometry" / (filename + ".py")))
            Point, Line = geom["Point"], geom["Line"]
            line = Line(Point(0, 0), Point(2, 2))
            cross = line.intersection(Line(Point(0, 2), Point(2, 0)))
            self.assertIsInstance(cross, Point)
            self.assertEqual(cross.as_tuple(), (1, 1))
            self.assertIsNone(line.intersection(line))
        union = lib("geometry/rectangle_union")["rectangle_union_area"]
        self.assertEqual(union([(0, 0, 2, 2), (1, 1, 3, 3), (0, 0, 2, 2)]), 7)
        self.assertEqual(union([]), 0)
        kd = lib("geometry/kd_tree")["KDTree"](points)
        self.assertEqual(sorted(kd.query(0, 0, 2, 2)), [0, 4, 5])
        plane = lib("geometry/plane_distance")["point_plane_distance"]
        self.assertEqual(plane((0, 0, 3), (0, 0, 0), (1, 0, 0), (0, 1, 0)), 3)

    def test_search(self):
        m = lib("search/heuristics")
        self.assertEqual(
            m["beam_search"](
                0, lambda x: [x + 1, x + 2], lambda x: x, lambda x: x, 2, 4
            ),
            8,
        )
        score, move = m["negamax"](
            3,
            5,
            lambda n: [x for x in (1, 2) if x <= n],
            lambda n, x: n - x,
            lambda n: -1 if n == 0 else 0,
            lambda n: n == 0,
        )
        self.assertEqual(score, -1)
        distance = [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
        tour = m["tsp_nearest_neighbor"](distance)
        self.assertEqual(tour, [0, 1, 2, 0])
        self.assertEqual(m["tsp_two_opt"](distance, tour), tour)
        m = lib("search/numeric")
        self.assertEqual(m["normal_cdf"](0), 0.5)
        labels, centers = m["kmeans"]([(0, 0), (0, 1), (10, 10), (10, 11)], 2)
        self.assertEqual(labels[0], labels[1])
        self.assertNotEqual(labels[0], labels[2])


if __name__ == "__main__":
    unittest.main()
