class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unq_lst = sorted(set(nums)) 
        max_val = 0
        counter = 1  

        if not unq_lst:
            return 0

        for i in range(1, len(unq_lst)):
            if unq_lst[i] == unq_lst[i - 1] + 1:
                counter += 1
            else:
                max_val = max(max_val, counter)
                counter = 1  

        return max(max_val, counter)
                