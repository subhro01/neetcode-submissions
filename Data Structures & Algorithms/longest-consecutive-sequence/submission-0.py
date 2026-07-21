class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            count = 0
            if num - 1 not in numset:
                curr = num
                while curr in numset:
                    curr += 1
                    count += 1

            res = max(count, res)
        
        return res