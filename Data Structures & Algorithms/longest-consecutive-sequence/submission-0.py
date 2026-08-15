from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashset = set(nums)
        for idx in range(len(nums)):
            number = nums[idx]
            if number - 1 not in hashset:
                lensequence = 1
                next_num = number + 1
                while next_num in hashset:
                    lensequence += 1
                    next_num += 1
                longest = max(longest, lensequence)
        return longest
        



            


    
                

        

        
        