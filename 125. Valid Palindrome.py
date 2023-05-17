import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^A-Z0-9]', '', s)
        for i in range(0, int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        
s = Solution()
print(s.isPalindrome("ab_a"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))