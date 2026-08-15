class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        longest  = 0
        count_dict = {}
        max_char = 0

        left = 0
        right = 0

        while right < len(s):
            count_dict[s[right]] = count_dict.get(s[right], 0) + 1
            max_char =  max(count_dict[s[right]], max_char)
            if right - left - max_char + 1 > k:
                count_dict[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
            


        
        
                

        

        
        


        