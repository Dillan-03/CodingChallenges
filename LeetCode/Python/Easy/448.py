class Solution:
    def findDisappearedNumbers(nums):
        holder = []
        for i in range(1, len(nums)+1):
            if i not in set(nums):
                holder.append(i)
        print(holder)

