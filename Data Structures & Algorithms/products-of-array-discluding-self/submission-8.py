class Solution:
    from collections import defaultdict
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        prefix_sum[0] = 1
        suffix_sum[n -1] = 1
        for i in range(1, n):
            prefix_sum[i] =  nums[i - 1] * prefix_sum[i -1]
        for i in range(n -2, -1, -1):
            suffix_sum[i] = nums[i + 1] * suffix_sum[i+1]
        for i in range(n):
            products[i] = prefix_sum[i] * suffix_sum[i]
        return products
    
        

            

        

        
            

        