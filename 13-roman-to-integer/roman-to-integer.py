class Solution:
    def romanToInt(self, s: str) -> int:
        hashm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            val = hashm[s[i]]
            if i + 1 < len(s) and val < hashm[s[i + 1]]:
                total -= val
            else:
                total += val

        return total