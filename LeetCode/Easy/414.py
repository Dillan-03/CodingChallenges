class Solution:
    def thirdMax(self, nums) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        if len(nums) > 3:
            return nums[-1]
        else:
            return nums[-3]
x = Solution()
print(x.thirdMax([-1,2,3]))