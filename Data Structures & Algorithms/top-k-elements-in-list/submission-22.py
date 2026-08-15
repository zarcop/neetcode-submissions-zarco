class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for i in range(len(nums)):
            if nums[i] not in freq_dict:
                freq_dict[nums[i]] = 1
            else:
                freq_dict[nums[i]] += 1
        list_of_freq = []
        for vals, freq in freq_dict.items():
            list_of_freq.append([freq, vals])
        list_of_freq.sort()
        list_of_freq = list_of_freq[::-1]
        final_list = []
        for i in range(k):
            final_list.append(list_of_freq[i][1])
        return final_list
        