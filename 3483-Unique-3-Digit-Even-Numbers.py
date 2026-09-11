class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_nums = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        hundreds = digits[i]
                        tens = digits[j]
                        ones = digits[k]
                        
                        # Check conditions: no leading zero and ones place must be even
                        if hundreds != 0 and ones % 2 == 0:
                            num = hundreds * 100 + tens * 10 + ones
                            unique_nums.add(num)
                            
        return len(unique_nums)