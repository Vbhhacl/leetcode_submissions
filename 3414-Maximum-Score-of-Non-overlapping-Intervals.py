from bisect import bisect_left
from typing import List


class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store intervals as (l, r, w, orig_idx) sorted by start time
        A = sorted(
            (l, r, w, idx) for idx, (l, r, w) in enumerate(intervals)
        )
        starts = [x[0] for x in A]

        # dp[c][i] = (-max_weight, lexicographically_smallest_indices_tuple)
        # choosing at most c intervals from suffix A[i:]
        dp = [[(0, ())] * (n + 1) for _ in range(5)]

        for i in range(n - 1, -1, -1):
            l, r, w, orig_idx = A[i]
            # Find the first interval that starts strictly after r
            nxt = bisect_left(starts, r + 1)

            for c in range(1, 5):
                # Option 1: Do not choose interval A[i]
                best = dp[c][i + 1]

                # Option 2: Choose interval A[i]
                rem_w, rem_indices = dp[c - 1][nxt]
                cand_w = rem_w - w
                cand_indices = tuple(sorted((orig_idx,) + rem_indices))
                cand = (cand_w, cand_indices)

                if cand < best:
                    best = cand

                dp[c][i] = best

        return list(dp[4][0][1])