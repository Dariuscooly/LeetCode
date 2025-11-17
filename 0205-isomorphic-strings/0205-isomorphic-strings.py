class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        index = {}
        pointer_one, pointer_two = 0, 0
        while pointer_one < len(s):
            if s[pointer_one] not in index:
                index[s[pointer_one]] = t[pointer_two]
            if index[s[pointer_one]] != t[pointer_two]:
                return False
            pointer_one += 1
            pointer_two += 1
        return True
                
            


        