from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        
        window_dict = {}

        required = len(dict_t)

        min_len = float('inf')
        valid = ""
        formed = 0

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_dict[char] = window_dict.get(char, 0) + 1
            if char in dict_t and dict_t[char] == window_dict[char]:
                formed += 1
            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < min_len:
                    min_len = right-left + 1
                    valid = s[left:right + 1]
                window_dict[char] -= 1
                if char in dict_t and window_dict[char] < dict_t[char]:
                    formed -= 1
                left += 1
        return valid
   

            

            
            


            
        