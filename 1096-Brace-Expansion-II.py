class Solution:

    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0
        n = len(expression)

        def parse_expr() -> set[str]:
            nonlocal i
            res = set()
            # An Expression is one or more Terms separated by ',' (Union)
            while i < n:
                res.update(parse_term())
                if i < n and expression[i] == ",":
                    i += 1  # skip ','
                else:
                    break
            return res

        def parse_term() -> set[str]:
            nonlocal i
            # A Term is one or more Factors concatenated together (Cartesian product)
            res = {""}  # Identity set for string concatenation
            while i < n and (expression[i].isalpha() or expression[i] == "{"):
                factor = parse_factor()
                res = {s + t for s in res for t in factor}
            return res

        def parse_factor() -> set[str]:
            nonlocal i
            if expression[i] == "{":
                i += 1  # skip '{'
                res = parse_expr()
                i += 1  # skip '}'
                return res
            else:
                ch = expression[i]
                i += 1
                return {ch}

        # Return unique words sorted lexicographically
        return sorted(list(parse_expr()))