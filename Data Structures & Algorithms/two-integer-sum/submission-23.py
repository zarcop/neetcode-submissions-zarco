class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        
        for j in range(len(nums)):
            difference = target - nums[j]
            if difference in indices and indices[difference] != j:
                return[j , indices[difference]]

        
        