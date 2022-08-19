class Solution:
    def getConcatenation(self, nums):
        holder = nums.copy()
        for x in range(0,len(nums)):
            holder.append(nums[x])
        return holder
x = Solution()
print(x.getConcatenation([1,2,1]))