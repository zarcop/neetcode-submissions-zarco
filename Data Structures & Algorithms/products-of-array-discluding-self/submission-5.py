class Solution:
    from collections import defaultdict
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            multiplication = 1
            j =  0
            k = len(nums) - 1
            while j < i:
                multiplication *= nums[j]
                j += 1
            while k > i:
                multiplication *= nums[k]
                k -= 1
            products.append(multiplication)
        return products
        

        
            

        