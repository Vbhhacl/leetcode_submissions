class Solution:

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        # Record the first and last occurrence index for each character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Find valid minimal intervals starting at first[ch] for each unique character
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True

            i = l
            while i <= r:
                # If a character inside [l, r] started before l, l cannot be a valid start
                if first[s[i]] < l:
                    valid = False
                    break
                r = max(r, last[s[i]])
                i += 1

            if valid:
                intervals.append((r, l))

        # Sort valid intervals by their end index
        intervals.sort()

        ans = []
        prev_end = -1

        # Greedily select non-overlapping intervals
        for r, l in intervals:
            if l > prev_end:
                ans.append(s[l : r + 1])
                prev_end = r

        return ans