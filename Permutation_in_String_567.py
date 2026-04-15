class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):

            return False

        #2 arrays of size 26, array index 0 = a etc

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for letter in s1:

            s1_counts[ord(letter) - ord('a')] += 1

        for i in range (len(s1)):

            s2_counts[ord(s2[i]) - ord('a')] += 1

        for i in range (len(s1), len(s2)):

            if s2_counts == s1_counts: return True

            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - len(s1)]) - ord('a')]-= 1

        return s2_counts == s1_counts
