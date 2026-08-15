class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [0] * len(nums)
        suffix_array = [0] * len(nums)
        prefix_array[0] = 1
        suffix_array[len(nums)-1] = 1
        
        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i - 1] * nums[i- 1]
        for  i in range(len(nums) -2, -1, -1):
            suffix_array[i] = suffix_array[i + 1] * nums[i+1]
        product = [0] * len(nums)
        for i in range(len(nums)):
            product[i] = suffix_array[i] * prefix_array[i]
        return product


      
        
        

        


        