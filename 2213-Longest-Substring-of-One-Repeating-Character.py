class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def merge(a, b):

            length = a[5] + b[5]

            prefix = a[2]
            suffix = b[3]

            best = max(a[4], b[4])

            if a[1] == b[0]:

                best = max(best, a[3] + b[2])

                # Entire left segment is one character
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # Entire right segment is one character
                if b[3] == b[5]:
                    suffix = b[5] + a[3]

            return [
                a[0],              # left character
                b[1],              # right character
                prefix,
                suffix,
                best,
                length
            ]

        def update(node, l, r, index, char):

            if l == r:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):

            update(1, 0, n - 1, index, char)

            ans.append(tree[1][4])

        return ans