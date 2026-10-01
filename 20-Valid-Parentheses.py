class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_bracket:
                # Character is a closing bracket
                top_element = stack.pop() if stack else '#'
                if matching_bracket[char] != top_element:
                    return False
            else:
                # Character is an opening bracket
                stack.append(char)
                
        # Return True if all open brackets were matched and popped
        return not stack