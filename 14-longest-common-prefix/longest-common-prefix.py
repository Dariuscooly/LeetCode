class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""

        for tup in zip(*strs):
            if len(set(tup)) > 1:
                return prefix
            
            prefix += tup[0]

        return prefix
                    