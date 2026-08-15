class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        final_list = []
        for word in strs:
            frequency = [0] * 26
            for char in word:
                ordinal = ord(char) - ord("a")
                frequency[ordinal] += 1
            key_list = tuple(frequency)
            if key_list not in dictionary:
                dictionary[key_list] = [word]
            else:
                dictionary[key_list].append(word)
        for freqs in dictionary:
            final_list.append(dictionary[freqs])
        return final_list