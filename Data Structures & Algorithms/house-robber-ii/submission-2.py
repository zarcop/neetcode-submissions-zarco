class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        array_1 = nums[1:]
        array_2 = nums[:-1]

        def rob(i, array, cache):
            if i >= len(array):
                return 0
            if i in cache:
                return cache[i]
            cache[i] =  max(array[i] + rob(i + 2, array, cache), rob(i+1, array, cache))
            return cache[i]
        

        return max(rob(0, array_1, {}), rob(0, array_2, {}))
            





        



        