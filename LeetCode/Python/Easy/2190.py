# Most Frequent Number Following Key In an Array

class Solution:
    def mostFrequent(self, nums, key: int) -> int:
        holder = []
        for number in nums:
            holder.append(number)

