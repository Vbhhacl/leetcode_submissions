class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        res = []
        in_bracket = False
        curr_key = []

        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                key_str = "".join(curr_key)
                res.append(d.get(key_str, "?"))
                in_bracket = False
                curr_key = []
            elif in_bracket:
                curr_key.append(char)
            else:
                res.append(char)

        return "".join(res)