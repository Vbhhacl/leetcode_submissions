class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # Edge cases:
        if target < 0:
            return -1  # Impossible to reach x because total sum is less than x
        if target == 0:
            return len(nums)  # We need to take all elements
        
        left = 0
        current_sum = 0
        max_len = -1
        
        # Sliding window to find the longest subarray summing to target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window from the left if sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # Record maximum length if exact target is reached
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1