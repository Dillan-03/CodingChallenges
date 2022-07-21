#Running Sum of 1d array 
class Solution:
    def runningSum(self, nums):
        total = [] 
        for i in range(1,len(nums)+1):
            total.append(sum(nums[0:i]))
        return total


x = Solution()
print(x.runningSum([1,2,3,4]))