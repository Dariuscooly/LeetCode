class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        output = 0
        
        # Loop through the string, stopping 2 characters before the end to get substrings of length 3
        for i in range(len(s) - 2):
            substring = s[i:i+3]  # Get the current substring of length 3
            
            # If the set of the substring has 3 unique characters, it's a good substring
            if len(set(substring)) == 3:
                output += 1
        
        return output
             