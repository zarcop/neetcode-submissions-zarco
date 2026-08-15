class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index , number in enumerate(nums):
            hashMap[number] = index
        for index, number in enumerate(nums):
            diff = target - number
            if diff in hashMap and hashMap[diff] != index:
                return [index, hashMap[diff]]
    

        