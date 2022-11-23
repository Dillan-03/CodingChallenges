from ssl import OP_NO_COMPRESSION


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ones = 0
        counter = 0
        # while counter <= len(nums):
        for i in range(0,len(nums)):
            if (nums[i] == 1):
                ones += 1 
            else:
                ones = 0
                    # return ones

            # counter += 1
        return ones

x = Solution()
print(x.findMaxConsecutiveOnes([1,0,1,1,0,1]))