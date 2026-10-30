class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in indices and indices[diff] != j:
                return [j, indices[diff]]
                
            
        

        
        