class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        positions = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            x = nums[right]

            if x not in positions:
                positions[x] = []

            positions[x].append(right)

            if len(positions[x]) > k:
                left = positions[x][-k - 1] + 1

            ans = max(ans, right - left + 1)

        return ans