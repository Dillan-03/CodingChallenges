# Missing Number
class Solution:
    def missingNumber(self, nums):
        # minimum = min(nums)
        # maximum = max(nums)
        # for i in range(0, maximum+1):
        #     if i not in nums:
        #         return i
        print(len(nums))
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i


x = Solution()
print(x.missingNumber([0]))
