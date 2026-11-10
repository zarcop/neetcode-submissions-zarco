from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

    
        table = {}

        for num in nums:
            if num in table:
                return num
            else:
                table[num] = 1
            



        
        