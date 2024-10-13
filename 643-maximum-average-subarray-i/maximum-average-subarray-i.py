class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for n in range(k,len(nums)):
            currSum += nums[n] - nums[n - k]
            maxSum = max(currSum, maxSum)
        return maxSum / k
            
            
        
        
        # maximum = 0
        # for i in range(len(nums) - k +1):
            
        #     ave = sum(nums[i:k+i])/k
        #     if ave > maximum:
        #         maximum = ave

        
        # if len(nums) == 1:
        #     maximum = nums[0]
        # elif len(nums) == 0:
        #     return 0
        # return maximum 

