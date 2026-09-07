class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends_with = {}

        for char in s:
            # New subsequences ending with 'char' = (All existing distinct subsequences) + 1 (for 'char' itself)
            ends_with[char] = (sum(ends_with.values()) + 1) % MOD

        return sum(ends_with.values()) % MOD