class Solution:
    paring_map = {}

    def __init__(self):
        self.paring_map['('] = ')'
        self.paring_map[')'] = '('
        self.paring_map['{'] = '}'
        self.paring_map['}'] = '{'
        self.paring_map['['] = ']'
        self.paring_map[']'] = '['

    def is_starting_bracket(self, s: str):
        if not len(s) == 1:
            return False
        return s[0] == '(' or s[0] == '{' or s[0] == '['

    def is_ending_bracket(self, s: str):
        if not len(s) == 1:
            return False
        return s[0] == ')' or s[0] == '}' or s[0] == ']'

    def isValid(self, s: str) -> bool:
        starting_brackets = []
        for i in range(0, len(s)):
            current_char = s[i]
            if self.is_starting_bracket(current_char):
                starting_brackets.append(current_char)
            elif self.is_ending_bracket(current_char):
                size = len(starting_brackets)
                if size == 0:
                    return False

                # pop last element
                elif not starting_brackets.pop() == self.paring_map[
                    current_char]:
                    return False

        if not len(starting_brackets) == 0:
            return False
        return True


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
