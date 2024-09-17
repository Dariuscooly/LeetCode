class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Length check
        if len(word1) != len(word2):
            return False
        
        # Step 2: Check if both words have the same set of characters
        if set(word1) != set(word2):
            return False
        
        # Step 3: Check if both words have the same character frequency distributions
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Sort the frequency values and compare
        return sorted(count1.values()) == sorted(count2.values())