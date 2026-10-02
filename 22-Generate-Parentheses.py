class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(current_str: str, open_count: int, close_count: int):
            # Base Case: valid string of length 2*n is formed
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Add '(' if we haven't reached the limit of 'n' open brackets
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Add ')' if it won't exceed the number of open brackets
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res