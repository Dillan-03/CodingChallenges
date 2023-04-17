# 283. Move Zeroes

def moveZeroes( nums):
    nums = list(nums)
    """
    Do not return anything, modify nums in-place instead.283.py
    
    """

    for zeros in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

moveZeroes([0,1,0,3,12])
