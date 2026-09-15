class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n
        
        for i in range(n):
            if i > 0:
                dp[i] = dp[i - 1]
            
            # Check palindrome of length k ending at index i
            if i - k + 1 >= 0:
                sub1 = s[i - k + 1 : i + 1]
                if sub1 == sub1[::-1]:
                    prev = dp[i - k] if i - k >= 0 else 0
                    dp[i] = max(dp[i], prev + 1)
            
            # Check palindrome of length k + 1 ending at index i
            if i - k >= 0:
                sub2 = s[i - k : i + 1]
                if sub2 == sub2[::-1]:
                    prev = dp[i - k - 1] if i - k - 1 >= 0 else 0
                    dp[i] = max(dp[i], prev + 1)
                    
        return dp[-1] if n > 0 else 0