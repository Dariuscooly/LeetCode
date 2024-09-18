class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        sorted_mp = sorted(mp.keys(), key=lambda word: (-mp[word], word))
            
        return sorted_mp[:k]