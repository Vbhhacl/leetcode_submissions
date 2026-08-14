class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26

        left = 0
        ans = 0

        for right in range(len(s)):

            index = ord(s[right]) - ord('a')
            count[index] += 1

            while count[index] > 2:
                left_index = ord(s[left]) - ord('a')
                count[left_index] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans