# Single Number
from collections import Counter


class Solution:
    def singleNumber(self, nums):
        holder = Counter(nums)

        for key, value in holder.items():
            if value == 1:
                return key


x = Solution()
print(x.singleNumber([2, 2, 3, 2]))
