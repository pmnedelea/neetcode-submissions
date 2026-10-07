class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        i = 0
        j = 0
        maximum = 0

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                if j - i + 1 > maximum:
                    maximum = j - i + 1
                
                j += 1


            else:
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                
                i += 1
                j += 1
                

        return maximum