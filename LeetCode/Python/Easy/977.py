# Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums):
        nums = sorted([i**2 for i in (nums)])
        return (nums)


x = Solution()
print(x.sortedSquares([-4, -1, 0, 3, 10]))
