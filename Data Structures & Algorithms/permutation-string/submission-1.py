class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
        
        j = 0
        for i in range(len(s2)):
            k = ord(s2[i]) - ord('a')
            freq_s2[k] += 1

            if i - j + 1 > len(s1):
                l = ord(s2[j]) - ord('a')
                freq_s2[l] -= 1
                j += 1
            
            if i - j + 1 == len(s1) and freq_s1 == freq_s2:
                return True
        
        return False