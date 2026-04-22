class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_occur,t_occur = {},{}

        for i in range(len(s)):
            s_occur[s[i]] = s_occur.get(s[i],0)+1
            t_occur[t[i]] = t_occur.get(t[i],0)+1
        return s_occur == t_occur
        