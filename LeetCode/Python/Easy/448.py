# Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(nums):
         return list(set(range(1,len(nums)+1)).difference(set(nums)))
