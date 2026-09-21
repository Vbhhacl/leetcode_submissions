from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            val = num % k
            next_dp = [0] * k
            
            # Subarray consisting of just the current element
            next_dp[val] += 1
            
            # Extend existing subarrays ending at the previous index
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val) % k] += dp[r]
            
            dp = next_dp
            
            # Add counts of all subarrays ending at the current index
            for r in range(k):
                ans[r] += dp[r]
                
        return ans