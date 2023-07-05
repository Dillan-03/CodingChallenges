# Find the Duplicate Number
from collections import Counter


class Solution:
    def findDuplicate(nums):
        holder = Counter(nums)
        for key, value in holder.items():
            if value > 1:
                return key


print(Solution.findDuplicate([1, 3, 4, 2, 2]))
