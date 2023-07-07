# Sort Colors

class Solution:
    def sortColors(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)


Solution.sortColors([2, 0, 2, 1, 1, 0])
