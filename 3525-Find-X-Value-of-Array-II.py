from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 1, 0, self.n - 1)

    def combine(self, node: int, left_node: int, right_node: int):
        k = self.k
        p_l = self.tree_prod[left_node]
        p_r = self.tree_prod[right_node]
        self.tree_prod[node] = (p_l * p_r) % k
        
        cnt_l = self.tree_cnt[left_node]
        cnt_r = self.tree_cnt[right_node]
        cnt_node = list(cnt_l)
        for r in range(k):
            c = cnt_r[r]
            if c:
                cnt_node[(p_l * r) % k] += c
        self.tree_cnt[node] = cnt_node

    def build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            v = nums[l] % self.k
            self.tree_prod[node] = v
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][v] = 1
            return
        mid = (l + r) // 2
        self.build(nums, 2 * node, l, mid)
        self.build(nums, 2 * node + 1, mid + 1, r)
        self.combine(node, 2 * node, 2 * node + 1)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            v = val % self.k
            self.tree_prod[node] = v
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][v] = 1
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self.combine(node, 2 * node, 2 * node + 1)

    def query(self, node: int, l: int, r: int, ql: int, qr: int, cur_prod: int, cur_cnt: List[int]) -> int:
        if ql <= l and r <= qr:
            k = self.k
            node_prod = self.tree_prod[node]
            node_cnt = self.tree_cnt[node]
            for rem in range(k):
                c = node_cnt[rem]
                if c:
                    cur_cnt[(cur_prod * rem) % k] += c
            cur_prod = (cur_prod * node_prod) % k
            return cur_prod
        
        mid = (l + r) // 2
        if ql <= mid:
            cur_prod = self.query(2 * node, l, mid, ql, qr, cur_prod, cur_cnt)
        if qr > mid:
            cur_prod = self.query(2 * node + 1, mid + 1, r, ql, qr, cur_prod, cur_cnt)
        return cur_prod

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []
        for idx, val, start, x in queries:
            st.update(1, 0, n - 1, idx, val)
            cur_cnt = [0] * k
            st.query(1, 0, n - 1, start, n - 1, 1, cur_cnt)
            ans.append(cur_cnt[x])
        return ans