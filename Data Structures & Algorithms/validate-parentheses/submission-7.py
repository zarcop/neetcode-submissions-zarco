class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")":"(", "}" : "{", "]": "["}
        for chars in s:
            if chars in dictionary:
                if stack and stack[-1] == dictionary[chars]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chars)
        if not stack:
            return True
        else:
            return False
            

                


        