class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = {}
        for num in arr:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
        retval = [i for i in mp.values()]

        return len(set(retval)) == len(retval)

