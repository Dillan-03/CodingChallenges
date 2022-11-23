class Solution:
    def removeElement(self, nums, val: int) -> int:
        
        while val in nums:
            nums.remove(val)
        return (len(nums))
        


x = Solution()
print(x.removeElement([3,2,2,3],3))