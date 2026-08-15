class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            if not stack:
                return False
            if char  == ")":
                if stack.pop() != "(":
                    return False
            elif char == "}":
                if stack.pop() != "{":
                    return False
            elif char == "]":
                if stack.pop() != "[":
                    return False
        if stack:
            return False
        return True




        