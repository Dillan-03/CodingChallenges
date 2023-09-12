# Single Element in a Sorted Array
class Solution:
    def singleNonDuplicate(self, nums):
        for i in range(0, len(nums), 2):
            if i == len(nums)-1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
        return None


x = Solution()
print(x.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
