class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for word in strs:
            string += (str(len(word)) + '#')
            string += word 
        return string

            


    def decode(self, s: str) -> List[str]:
        i = 0
        final_list = []
        while i < len(s):
            j = i
            numberstr = ''
            while s[j] != '#' and j < len(s):
                numberstr += s[j]
                j += 1
            number_range = int(numberstr)
            word = ''
            for k in range(j + 1, number_range + j + 1): # skip the hashtag
                word += s[k]
            final_list.append(word)
            i = number_range + j + 1
        return final_list
            


                



            


                

            
        
