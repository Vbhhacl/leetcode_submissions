class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        ans = float('inf')
        
        left = 0
        curr_sum = 0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
                
            if curr_sum == target:
                curr_len = right - left + 1
                
                # Check if a valid non-overlapping subarray exists prior to the current window
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                # Store the minimum subarray length up to index `right`
                min_len[right] = min(min_len[right - 1] if right > 0 else float('inf'), curr_len)
            else:
                min_len[right] = min_len[right - 1] if right > 0 else float('inf')
                
        return ans if ans != float('inf') else -1