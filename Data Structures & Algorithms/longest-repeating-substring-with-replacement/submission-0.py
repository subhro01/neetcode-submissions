class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = [0] * 26

        i, j = 0, 0
        res = 0
        freq_max = 0
        while i <= j and j < len(s):
            freq[ord(s[j]) - ord('A')] += 1
            freq_max = max(freq_max, freq[ord(s[j]) - ord('A')])
            if (j - i + 1) - freq_max <= k:
                res = max(res, j - i + 1)
            else:
                freq[ord(s[i]) - ord('A')] -= 1
                i += 1
            j += 1
        
        return res