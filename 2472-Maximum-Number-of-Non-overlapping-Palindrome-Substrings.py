class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = 0
        last_end = -1  # Index of the last character of the last selected palindrome
        
        for i in range(len(s)):
            # 1. Check window of length k ending at index i
            if i - k + 1 > last_end:
                sub = s[i - k + 1 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    continue  # Move to next index since this character is consumed
            
            # 2. Check window of length k + 1 ending at index i
            if i - k > last_end:
                sub = s[i - k : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    
        return ans