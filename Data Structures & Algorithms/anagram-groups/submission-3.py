class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for strings in strs:
            count = [0] * 26
            for c in strings:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(strings)
        return list(res.values())


            

            






     