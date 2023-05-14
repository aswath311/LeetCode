class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        a = [0] * 26
        for i in range(len(s)):
            a[ord(s[i])-97] += 1
            a[ord(t[i])-97] -= 1
        for i in a:
            if a[i] !=0: 
                return False
        return True

s = Solution()
print(s.isAnagram("anagram", "marganaa"))
        