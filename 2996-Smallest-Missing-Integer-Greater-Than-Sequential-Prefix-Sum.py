class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                total += nums[i + 1]
            else:
                break
        while total in nums:
            total += 1
        return total