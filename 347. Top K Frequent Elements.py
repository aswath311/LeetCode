class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        occurence = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for key, val in freq.items():
            occurence[val].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for n in occurence[i]:
                res.append(n)
                if(len(res) == k):
                    return res
        return res

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
