class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if i > 0 and numbers[i] == numbers[i-1]:
                i += 1
            sumNum = numbers[i] + numbers[j]
            if sumNum < target:
                i += 1
            elif sumNum > target:
                j -= 1
            else:
                return [i + 1,j + 1]

