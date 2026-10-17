"""_cp_structures.py の再現可能な回帰・ランダムテスト。
python _cp_structures_tests.py
"""

import importlib.util
import random
from collections import Counter, deque
from math import inf
from pathlib import Path

SRC = Path(__file__).with_name('_cp_structures.py')
spec = importlib.util.spec_from_file_location('cp_structures', SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TOTAL = 0

def eq(a,b,desc=''):
    global TOTAL
    TOTAL += 1
    assert a == b, (desc, a, b)


def raises(exception, fun):
    global TOTAL
    TOTAL += 1
    try:
        fun()
    except exception:
        return
    raise AssertionError(f'{exception.__name__} expected: {fun}')


def test_misc():
    v=mod.make_grid(2,3,7)
    v[0][0]=15
    eq(v,[[15,7,7],[7,7,7]])
    eq(mod.make_grid(0,2,1), [])


def test_kinddeque():
    rng=random.Random(140)
    for case in range(35):
        init=[rng.randrange(8) for _ in range(rng.randrange(20))]
        ref=deque(init)
        d=mod.KindDeque(init)
        for i in range(550):
            op=rng.randrange(9)
            if op==0:
                x=rng.randrange(8);d.append(x);ref.append(x)
            elif op==1:
                x=rng.randrange(8);d.appendleft(x);ref.appendleft(x)
            elif op==2 and ref:
                eq(d.pop(),ref.pop(),'KindDeque.pop')
            elif op==3 and ref:
                eq(d.popleft(),ref.popleft(),'KindDeque.popleft')
            elif op==4:
                vals=[rng.randrange(8) for _ in range(rng.randrange(6))]
                d.extend(vals);ref.extend(vals)
            elif op==5:
                vals=[rng.randrange(8) for _ in range(rng.randrange(6))]
                d.extendleft(vals);ref.extendleft(vals)
            elif op==6:
                k=rng.randrange(-50,51); d.rotate(k);ref.rotate(k)
            elif op==7 and i%19==0:
                d.clear();ref.clear()
            elif op==8 and ref:
                idx=rng.randrange(-len(ref),len(ref))
                eq(d[idx],ref[idx],'KindDeque.index')
            eq(list(d),list(ref),'KindDeque.content')
            co=Counter(ref)
            eq(d.kind,len(co),'KindDeque.kind')
            eq(d.C,co,'KindDeque.Counter')
            for x in (0,1,5,8):
                eq(d.count(x),co[x])
                eq((x in d), bool(co[x]))
    raises(IndexError,lambda:mod.KindDeque().pop())
    raises(IndexError,lambda:mod.KindDeque().popleft())


def norm_groups(groups):
    return sorted(tuple(sorted(g)) for g in groups)


def test_unionfind():
    rng=random.Random(120)
    for n in range(0,35):
        uf=mod.UnionFind(n)
        comp=list(range(n))
        for _ in range(300):
            if n==0:
                eq(uf.group_count(),0)
                eq(uf.groups(),[])
                break
            x,y=rng.randrange(n),rng.randrange(n)
            pre=comp[x]==comp[y]
            if rng.randrange(2):
                eq(uf.unite(x,y),not pre,'UF.unite')
            else:
                root=uf.merge(x,y)
                eq(root,uf.find(x),'UF.merge')
            old=comp[y]
            target=comp[x]
            comp=[target if v==old else v for v in comp]
            eq(uf.is_same(x,y),True)
            eq(uf.same(x,y),True)
            eq(uf.size(x),sum(c==comp[x] for c in comp))
            eq(uf.group_count(),len(set(comp)))
            if rng.randrange(30)==0:
                expected=norm_groups([[i for i in range(n) if comp[i]==c] for c in set(comp)])
                eq(norm_groups(uf.groups()),expected)
                eq(norm_groups(uf.all_group_members().values()),expected)
                eq(sorted(uf.members(x)),[i for i in range(n) if comp[i]==comp[x]])
        eq(len(uf),n)


def test_weighted_unionfind():
    rng=random.Random(90)
    for n in range(0,32):
        uf=mod.WeightedUnionFind(n)
        pots=[rng.randrange(-1000,1001) for _ in range(n)]
        label=list(range(n))
        for _ in range(450):
            if n==0:
                eq(uf.group_count(),0)
                eq(uf.weights(),[])
                break
            x,y=rng.randrange(n),rng.randrange(n)
            w=pots[y]-pots[x]
            old_same=label[x]==label[y]
            eq(uf.is_consistent(x,y,w),True)
            eq(uf.unite(x,y,w),not old_same)
            old,new=label[y],label[x]
            label=[new if a==old else a for a in label]
            eq(uf.is_same(x,y),True)
            eq(uf.diff(x,y),w)
            eq(uf.group_count(),len(set(label)))
            eq(uf.get_weight(x),pots[x]-pots[uf.find(x)])
            if rng.randrange(35)==0:
                eq(uf.is_consistent(x,y,w+1),False)
                raises(ValueError,lambda:uf.unite(x,y,w+1))
                eq(uf.diff(x,y),w)
                eq(norm_groups(uf.groups()),norm_groups([[i for i in range(n) if label[i]==c] for c in set(label)]))
                eq(uf.weights(),[pots[i]-pots[uf.find(i)] for i in range(n)])
        if n>=2:
            new=mod.WeightedUnionFind(n)
            raises(ValueError,lambda:new.diff(0,1))
        eq(len(uf),n)


def test_segtrees():
    rng=random.Random(283)
    for n in range(0,60):
        arr=[rng.randrange(-15,16) for _ in range(n)]
        sg=mod.segtree(arr,lambda a,b:a+b,0)
        old=mod.SegTree(arr,lambda a,b:a+b,0)
        eq(sg.to_list(),arr)
        eq(len(sg),n)
        eq(sg.all_prod(),sum(arr))
        for _ in range(140):
            if n and rng.randrange(4)==0:
                i=rng.randrange(n)
                x=rng.randrange(-25,26)
                if rng.randrange(2):
                    sg.set(i,x); old.update(i,x); arr[i]=x
                else:
                    v=x-arr[i];sg.set(i,x);old.add(i,v);arr[i]=x
                eq(sg.get(i),x)
                eq(sg[i],x)
                eq(old.get(i),x)
                eq(old.num,old.size)
                eq(old.tree,old.d)
            l=rng.randrange(n+1); r=rng.randrange(l,n+1)
            val=sum(arr[l:r])
            eq(sg.prod(l,r),val,'segtree.sum')
            eq(old.query(l,r),val,'SegTree.query')
            eq(old.prod(l,r),val)
            eq(sg.all_prod(),sum(arr))
        eq(sg.to_list(),arr)
    for n in range(0,42):
        arr=[rng.randrange(0,13) for _ in range(n)]
        sg=mod.segtree(arr,lambda a,b:a+b,0)
        for l in range(n+1):
            for threshold in (0,1,15,30,1000):
                x=l;s=0
                while x<n and s+arr[x]<=threshold:
                    s+=arr[x];x+=1
                eq(sg.max_right(l,lambda z,t=threshold:z<=t),x,'segtree.max_right')
        for r in range(n+1):
            for threshold in (0,1,15,30,1000):
                x=r;s=0
                while x>0 and s+arr[x-1]<=threshold:
                    x-=1;s+=arr[x]
                eq(sg.min_left(r,lambda z,t=threshold:z<=t),x,'segtree.min_left')
    for n in range(0,25):
        arr=[chr(ord('a')+rng.randrange(7)) for _ in range(n)]
        sg=mod.segtree(arr,lambda a,b:a+b,'')
        for l in range(n+1):
            for r in range(l,n+1):
                eq(sg.prod(l,r),''.join(arr[l:r]),'noncomm.segtree')
        for l in range(n+1):
            for k in range(n+1):
                eq(sg.max_right(l,lambda z,k=k:len(z)<=k),min(n,l+k))
        for r in range(n+1):
            for k in range(n+1):
                eq(sg.min_left(r,lambda z,k=k:len(z)<=k),max(0,r-k))
    for n in range(30):
        sg=mod.segtree(n,lambda a,b:a+b,0)
        eq(sg.to_list(),[0]*n)


def test_lazy():
    rng=random.Random(753)
    plus=lambda x,y:(x[0]+y[0],x[1]+y[1])
    mapping=lambda f,x:(x[0]+f*x[1],x[1])
    for n in range(0,37):
        arr=[rng.randrange(0,10) for _ in range(n)]
        seg=mod.lazy_segtree([(x,1) for x in arr],plus,(0,0),mapping,lambda f,g:f+g,0)
        eq(seg.all_prod(),(sum(arr),n))
        for _ in range(350):
            op=rng.randrange(7)
            if n and op==0:
                i=rng.randrange(n);x=rng.randrange(0,20)
                arr[i]=x;seg.set(i,(x,1))
            elif n and op==1:
                i=rng.randrange(n);x=rng.randrange(0,20)
                arr[i]+=x;seg.apply_point(i,x)
            elif op==2:
                l=rng.randrange(n+1);r=rng.randrange(l,n+1);x=rng.randrange(0,10)
                seg.apply(l,r,x)
                for i in range(l,r):arr[i]+=x
            elif op==3 and n:
                i=rng.randrange(n)
                eq(seg.get(i),(arr[i],1),'lazy.get')
            elif op==4:
                l=rng.randrange(n+1);r=rng.randrange(l,n+1)
                eq(seg.prod(l,r),(sum(arr[l:r]),r-l),'lazy.prod')
            elif op==5:
                l=rng.randrange(n+1)
                thresh=rng.randrange(100)
                expected=l;s=0
                while expected<n and s+arr[expected]<=thresh:
                    s+=arr[expected];expected+=1
                eq(seg.max_right(l,lambda v,thresh=thresh:v[0]<=thresh),expected,'lazy.max_right')
            else:
                r=rng.randrange(n+1)
                thresh=rng.randrange(100)
                expected=r;s=0
                while expected>0 and s+arr[expected-1]<=thresh:
                    expected-=1;s+=arr[expected]
                eq(seg.min_left(r,lambda v,thresh=thresh:v[0]<=thresh),expected,'lazy.min_left')
            eq(seg.all_prod(),(sum(arr),n),'lazy.all_prod')
        eq(seg.to_list(),[(x,1) for x in arr],'lazy.to_list')
    # 非可換な tuple 連結と区間代入操作（各項目を同じ記号に置換）
    op=lambda a,b:a+b
    mapping=lambda f,x:x if f is None else (f,)*len(x)
    composition=lambda f,g:g if f is None else f
    for n in range(0,31):
        arr=[rng.randrange(5) for _ in range(n)]
        sg=mod.lazy_segtree([(x,) for x in arr],op,(),mapping,composition,None)
        for _ in range(220):
            if rng.randrange(3)==0:
                l=rng.randrange(n+1);r=rng.randrange(l,n+1);x=rng.randrange(6)
                sg.apply(l,r,x)
                arr[l:r]=[x]*(r-l)
            else:
                l=rng.randrange(n+1);r=rng.randrange(l,n+1)
                eq(sg.prod(l,r),tuple(arr[l:r]),'lazy.noncomm.prod')
                k=rng.randrange(n+1)
                eq(sg.max_right(l,lambda z,k=k:len(z)<=k),min(n,l+k))
                eq(sg.min_left(r,lambda z,k=k:len(z)<=k),max(0,r-k))
        eq(sg.to_list(),[(x,) for x in arr])
    for n in range(10):
        sg=mod.lazy_segtree(n,lambda a,b:a+b,0,lambda f,x:x+f,lambda f,g:f+g,0)
        eq(sg.to_list(),[0]*n)


def test_bit():
    rng=random.Random(222)
    for n in range(0,60):
        arr=[rng.randrange(0,30) for _ in range(n)]
        ft=mod.BIT(arr)
        eq(ft.to_list(),arr)
        eq(len(ft),n)
        for _ in range(180):
            if n and rng.randrange(3)==0:
                i=rng.randrange(n)
                if rng.randrange(2):
                    x=rng.randrange(0,30)
                    ft.set(i,x);arr[i]=x
                else:
                    x=rng.randrange(0,30)
                    ft.add(i,x);arr[i]+=x
                eq(ft.get(i),arr[i])
            l=rng.randrange(n+1);r=rng.randrange(l,n+1)
            eq(ft.prod(l,r),sum(arr[l:r]),'BIT.prod')
            eq(ft.range_sum(l,r),sum(arr[l:r]))
            eq(ft.prefix_sum(r),sum(arr[:r]))
            eq(ft.sum(l-1),sum(arr[:l]))
            eq(ft.all_sum(),sum(arr))
            target=rng.randrange(0,sum(arr)+5)
            expected=next((i for i in range(n) if sum(arr[:i+1])>=target),n) if target>0 else 0
            eq(ft.lower_bound(target),expected,'BIT.lower_bound')
        eq(ft.to_list(),arr)
    for n in range(0,20):
        ft=mod.BIT(n)
        eq(ft.to_list(),[0]*n)
        for i in range(n):
            ft.add(i,-i)
        eq(ft.all_sum(),sum(-i for i in range(n)))


def test_lca():
    rng=random.Random(432)
    for n in range(1,130):
        edges=[(i,rng.randrange(1,i)) for i in range(2,n+1)]
        root=rng.randrange(1,n+1)
        tree=mod.LCATree(n,edges,root)
        eq(tree.root,root)
        eq(len(tree),n)
        adj=[[] for _ in range(n+1)]
        for a,b in edges:adj[a].append(b);adj[b].append(a)
        parent=[-1]*(n+1)
        depth=[-1]*(n+1)
        depth[root]=0
        stack=[root]
        for v in stack:
            for to in adj[v]:
                if to==parent[v]:continue
                parent[to]=v
                depth[to]=depth[v]+1
                stack.append(to)
        eq(tree.depth,depth)
        for _ in range(110):
            u,v=rng.randrange(1,n+1),rng.randrange(1,n+1)
            x,y=u,v
            chain=set()
            while x!=-1:
                chain.add(x);x=parent[x]
            while y not in chain:
                y=parent[y]
            lca=y
            eq(tree.get_LCA(u,v),lca,'LCA')
            eq(tree.lca(u,v),lca,'LCA.alias')
            dist=depth[u]+depth[v]-2*depth[lca]
            eq(tree.distance(u,v),dist,'LCA.distance')
            path=[];x=u
            while x!=lca:path.append(x);x=parent[x]
            path.append(lca)
            tail=[];x=v
            while x!=lca:tail.append(x);x=parent[x]
            path.extend(reversed(tail))
            eq(tree.get_path(u,v),path,'LCA.path')
            k=rng.randrange(0,dist+3)
            eq(tree.jump(u,v,k),path[k] if k<len(path) else -1,'LCA.jump')
            k=rng.randrange(0,depth[u]+3)
            x=u
            for _ in range(k):x=parent[x] if x!=-1 else -1
            eq(tree.kth_ancestor(u,k),x,'LCA.kth_ancestor')
            x=v;on_chain=False
            while x!=-1:
                if x==u:on_chain=True
                x=parent[x]
            eq(tree.is_ancestor(u,v),on_chain,'LCA.is_ancestor')
            eq(tree.subtree_size(u),sum(tree.is_ancestor(u,z) for z in range(1,n+1)),'LCA.subtree_size')
    raises(ValueError,lambda:mod.LCATree(3,[(1,2)],1))
    raises(ValueError,lambda:mod.LCATree(3,[(1,2),(2,3),(3,1)],1))
    raises(ValueError,lambda:mod.LCATree(1,[(1,1)],1))
    raises(ValueError,lambda:mod.LCATree(0,[],1))


def test_deque():
    rng=random.Random(102)
    for case in range(34):
        ini=[rng.randrange(-20,21) for _ in range(rng.randrange(24))]
        d=mod.Deque(ini,max_size=rng.randrange(1,9))
        q=deque(ini)
        for _ in range(800):
            op=rng.randrange(10)
            if op==0:
                x=rng.randrange(-100,101);d.append(x);q.append(x)
            elif op==1:
                x=rng.randrange(-100,101);d.appendleft(x);q.appendleft(x)
            elif op==2:
                if q:eq(d.pop(),q.pop(),'Deque.pop')
                else:raises(IndexError,d.pop)
            elif op==3:
                if q:eq(d.popleft(),q.popleft(),'Deque.popleft')
                else:raises(IndexError,d.popleft)
            elif op==4:
                k=rng.randrange(-100,101);d.rotate(k);q.rotate(k)
            elif op==5:
                x=[rng.randrange(12) for _ in range(rng.randrange(5))]
                d.extend(x);q.extend(x)
            elif op==6:
                x=[rng.randrange(12) for _ in range(rng.randrange(5))]
                d.extendleft(x);q.extendleft(x)
            elif op==7 and q:
                i=rng.randrange(-len(q),len(q))
                eq(d[i],q[i],'Deque.index')
                val=rng.randrange(12);d[i]=val;q[i]=val
            elif op==8 and rng.randrange(8)==0:
                d.clear();q.clear()
            elif op==9:
                eq(list(reversed(d)),list(reversed(q)))
                eq(d.is_empty(),not q)
                eq(d.is_full(),len(d)==d.N)
            eq(list(d),list(q),'Deque.content')
            eq(len(d),len(q))
        eq(str(d),f'Deque({list(q)!r})')
    raises(IndexError,lambda:mod.Deque()[0])
    raises(IndexError,lambda:mod.Deque()[1])


def test_heapq():
    rng=random.Random(933)
    for n in range(0,26):
        initial=[rng.randrange(-15,16) for _ in range(n)]
        h=mod.Heapq(initial)
        ref=initial[:]
        for _ in range(950):
            op=rng.randrange(6)
            if op==0:
                x=rng.randrange(-20,21);h.push(x);ref.append(x)
            elif op==1:
                x=rng.randrange(-20,21)
                result=x in ref
                eq(h.erase(x),result,'heapq.erase')
                if result:ref.remove(x)
            elif op==2:
                expected=min(ref) if ref else None
                eq(h.pop(),expected,'heapq.pop')
                if ref:ref.remove(expected)
            elif op==3:
                eq(h.top(),min(ref) if ref else None,'heapq.top')
            elif op==4:
                values=[rng.randrange(-15,16) for _ in range(rng.randrange(12))]
                h.build(values)
                ref=values[:]
                eq(values,ref,'heapq.build input unchanged')
            else:
                eq(h.pop('EMPTY') if not ref else h.top('EMPTY'), 'EMPTY' if not ref else min(ref))
            eq(len(h),len(ref),'heapq.len')
            eq(bool(h),bool(ref),'heapq.bool')
            eq(h.top(),min(ref) if ref else None,'heapq.top-check')
            for x in (-20,-2,0,5,20):
                eq(h.count(x),ref.count(x),'heapq.count')
                eq(x in h,x in ref,'heapq.contains')
    h=mod.Heapq()
    eq(h.erase(4),False)
    h.push(4)
    eq(h.pop(),4)
    eq(h.top(),None)
    x=[3,2,1]
    h.build(x)
    h.pop()
    eq(x,[3,2,1])


def test_beats():
    rng=random.Random(32109)
    for case in range(230):
        n=case%55
        arr=[rng.randrange(-100,101) for _ in range(n)]
        if case%6==0:
            arr=[10**24+i for i in arr]
        if case%7==0:
            arr=[-10**24+i for i in arr]
        if case%9==0:
            arr=[0]*n
        st=mod.SegmentTreeBeats(n,arr)
        eq(len(st),n)
        for t in range(350):
            op=rng.randrange(11)
            l=rng.randrange(n+1);r=rng.randrange(l,n+1)
            x=rng.randrange(-300,301)
            if case%6==0 and rng.randrange(10)==0:x=10**24+x
            if case%7==0 and rng.randrange(10)==0:x=-10**24+x
            if op==0:
                st.update_min(l,r,x)
                arr[l:r]=[min(v,x) for v in arr[l:r]]
            elif op==1:
                st.update_max(l,r,x)
                arr[l:r]=[max(v,x) for v in arr[l:r]]
            elif op==2:
                st.add_val(l,r,x)
                arr[l:r]=[v+x for v in arr[l:r]]
            elif op==3:
                st.update_val(l,r,x)
                arr[l:r]=[x]*(r-l)
            elif op==4 and n:
                i=rng.randrange(n)
                st.set(i,x);arr[i]=x
                eq(st.get(i),arr[i],'beats.set/get')
            elif op==5:
                st.range_chmin(l,r,x)
                arr[l:r]=[min(v,x) for v in arr[l:r]]
            elif op==6:
                st.range_chmax(l,r,x)
                arr[l:r]=[max(v,x) for v in arr[l:r]]
            elif op==7:
                st.range_add(l,r,x)
                arr[l:r]=[v+x for v in arr[l:r]]
            elif op==8:
                st.range_assign(l,r,x)
                arr[l:r]=[x]*(r-l)
            elif op==9 and n:
                i=rng.randrange(n)
                eq(st.get(i),arr[i],'beats.get')
            else:
                eq(st.to_list(),arr,'beats.to_list')
            expected=(min(arr[l:r],default=inf),max(arr[l:r],default=-inf),sum(arr[l:r]))
            eq(st.query_min(l,r),expected[0],'beats.query_min')
            eq(st.query_max(l,r),expected[1],'beats.query_max')
            eq(st.query_sum(l,r),expected[2],'beats.query_sum')
            eq(st.query(l,r),expected,'beats.query')
            eq(st.all_min(),min(arr,default=inf),'beats.all_min')
            eq(st.all_max(),max(arr,default=-inf),'beats.all_max')
            eq(st.all_sum(),sum(arr),'beats.all_sum')
        eq(st.to_list(),arr,'beats.final_to_list')
    for n in range(25):
        st=mod.SegmentTreeBeats(n)
        eq(st.to_list(),[0]*n)
        st.update_max(0,n,5)
        eq(st.all_sum(),5*n)
        st.update_min(0,n,2)
        eq(st.to_list(),[2]*n)
    # 絶対値が 10^18 を超えるデータでセンチネルの取り違えがないこと
    st=mod.SegmentTreeBeats([10**60,-10**60,0])
    eq(st.query(0,3),(-10**60,10**60,0))
    st.range_chmax(0,3,10**30)
    eq(st.to_list(),[10**60,10**30,10**30])


def main():
    import time
    start=time.perf_counter()
    tests=[test_misc,test_kinddeque,test_unionfind,test_weighted_unionfind,
           test_segtrees,test_lazy,test_bit,test_lca,test_deque,test_heapq,test_beats]
    for f in tests:
        before=TOTAL
        t0=time.perf_counter()
        f()
        print(f'PASS {f.__name__:<27} {TOTAL-before:>9,} checks / {time.perf_counter()-t0:.2f}s')
    print(f'ALL PASS: {TOTAL:,} checks, {len(tests)} suites, {time.perf_counter()-start:.2f}s')


if __name__ == '__main__':
    main()
