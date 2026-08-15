class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = [0] * len(height)
        suffix = [0] * len(height)
        pref = height[0]
        suf = height[len(height) -1]
        area = 0

        for i in range(len(height)):
            pref = max(height[i],pref)
            prefix[i] = pref
        for i in range(len(height) -1, -1, -1):
            suf = max(suf, height[i])
            suffix[i] = suf
        
        for i in range(len(height)):
            area += (min(suffix[i], prefix[i]) -height[i])
        
        return area



            
            
        