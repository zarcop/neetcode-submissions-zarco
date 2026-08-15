class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for s in strs:
            final_str += str(len(s))
            final_str += "#"
            final_str += s
        return final_str


    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0
        while i <len(s):
            j = i
            while s[j] != "#":
                j += 1
            string_length = int(s[i:j])
            i = j + 1
            j = i + string_length
            final_list.append(s[i:j])
            i = j
        return final_list

                

            
            



    
