class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        original_counts = Counter(s)
        modified_counts = Counter(t)

        for ch in modified_counts:
            if modified_counts[ch] != original_counts.get(ch, 0):
                return ch