class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counterDict = {}
        for index in range(len(nums)):
            if nums[index] in counterDict:
                return True
            else:
                counterDict[nums[index]] = 1
        return False
        
        