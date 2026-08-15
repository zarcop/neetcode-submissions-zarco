class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Move left pointer past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1

            # If pointers haven't crossed and characters don't match (case-insensitive)
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            # If they matched, or if one of the while loops caused left >= right
            # then move both pointers inward
            left += 1
            right -= 1
            
        return True # If the loop completes, it's a palindrome
        


    

 


        