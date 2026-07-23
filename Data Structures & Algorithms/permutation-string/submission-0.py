class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
        
        i, j = 0, 0

        while i <= j and j < len(s2):
            while j < i + len(s1):
                freq_s2[ord(s2[j]) - ord('a')] += 1
                j += 1
            
            if freq_s1 == freq_s2:
                return True
            else:
                freq_s2[ord(s2[i]) - ord('a')] -= 1
                i += 1

        
        return False