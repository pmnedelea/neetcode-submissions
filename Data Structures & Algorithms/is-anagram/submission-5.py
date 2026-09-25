import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)) or (set(s) != set(t)):
            return False
        
        dict_s = {letter: 0 for letter in string.ascii_lowercase}
        dict_t = {letter: 0 for letter in string.ascii_lowercase}

        for i in range(len(s)):
            dict_s[s[i]] += 1
            dict_t[t[i]] += 1
        
        return dict_s == dict_t
        

        