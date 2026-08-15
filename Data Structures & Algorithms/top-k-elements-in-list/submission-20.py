from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        kList = []
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        counterList = list(hashmap.items())
        counterList.sort(key = lambda x : x[1])
        counterList.reverse()
        print(counterList)
        for j in range(k):
            kList.append(counterList[j][0])
        return kList
            


            
       
            
        



        