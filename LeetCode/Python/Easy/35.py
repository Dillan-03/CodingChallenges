class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
         

x = Solution()
print(x.searchInsert([4,3,2,1],2))