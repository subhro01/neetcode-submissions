class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        words = set()

        i, j = 0, 0
        count = 0

        while i <= j and j < len(s):
            while j < len(s) and s[j] not in words:
                words.add(s[j])
                j += 1
                count = max(count, j - i)
            else:
                if i < len(s) and s[i] in words:
                    words.remove(s[i])
                    i += 1
                count = max(count, j - i)
        
        return count