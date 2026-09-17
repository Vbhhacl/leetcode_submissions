class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        # If total flowers needed exceed total flowers available
        if m * k > len(bloomDay):
            return -1

        # Helper function to check if m bouquets can be formed on a given day
        def canMake(day: int) -> bool:
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0  # Reset adjacent counter if flower hasn't bloomed
            
            return bouquets >= m

        # Binary search range
        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                ans = mid
                high = mid - 1  # Try finding an earlier valid day
            else:
                low = mid + 1   # Need more days for flowers to bloom

        return ans