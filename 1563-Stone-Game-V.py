class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # Build prefix sums for O(1) range sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][k] stores the max of (dp[i][m] + pref[m+1]) for m in range [i, k]
        max_left = [[0] * n for _ in range(n)]
        
        # max_right[k][j] stores the max of (dp[m][j] - pref[m]) for m in range [k, j]
        max_right = [[0] * n for _ in range(n)]

        # Base case (length 1)
        for i in range(n):
            max_left[i][i] = pref[i + 1]
            max_right[i][i] = -pref[i]

        # Iterate over subarray lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Binary search for the largest mid_k in [i, j - 1] such that left_sum <= right_sum
                # left_sum <= right_sum translates to: 2 * pref[k + 1] <= pref[i] + pref[j + 1]
                target = (pref[i] + pref[j + 1]) / 2.0
                low, high = i, j - 1
                mid_k = i - 1

                while low <= high:
                    m = (low + high) // 2
                    if pref[m + 1] <= target:
                        mid_k = m
                        low = m + 1
                    else:
                        high = m - 1

                ans = 0

                # Edge case: If exactly equal at mid_k, Alice gets to pick
                if mid_k >= i and (pref[mid_k + 1] - pref[i]) * 2 == (pref[j + 1] - pref[i]):
                    ans = max(ans, (pref[mid_k + 1] - pref[i]) + max(dp[i][mid_k], dp[mid_k + 1][j]))
                    
                    if mid_k - 1 >= i:
                        ans = max(ans, max_left[i][mid_k - 1] - pref[i])
                    if mid_k + 2 <= j:
                        ans = max(ans, max_right[mid_k + 2][j] + pref[j + 1])
                else:
                    # Normal case: Left part thrown away for m <= mid_k, Right part thrown away for m > mid_k
                    if mid_k >= i:
                        ans = max(ans, max_left[i][mid_k] - pref[i])
                    if mid_k + 2 <= j:
                        ans = max(ans, max_right[mid_k + 2][j] + pref[j + 1])

                dp[i][j] = ans
                
                # Expand our tracking arrays for the next iterations
                max_left[i][j] = max(max_left[i][j - 1], dp[i][j] + pref[j + 1])
                max_right[i][j] = max(max_right[i + 1][j], dp[i][j] - pref[i])

        return dp[0][n - 1]