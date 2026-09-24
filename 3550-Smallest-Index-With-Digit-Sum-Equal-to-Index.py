class Solution:

    def smallestIndex(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate sum of digits for nums[i]
            digit_sum = sum(int(d) for d in str(num))

            # Return the first (smallest) index that matches
            if digit_sum == i:
                return i

        # Return -1 if no index satisfies the condition
        return -1