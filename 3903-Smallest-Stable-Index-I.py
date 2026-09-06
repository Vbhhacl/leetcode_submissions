class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Build suffix minimum array where suffix_min[i] stores min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # Track prefix maximum and check the condition for the smallest index i
        prefix_max = float('-inf')
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suffix_min[i] <= k:
                return i
                
        return -1