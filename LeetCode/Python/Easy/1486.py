#XOR Operation in an Array
class Solution(object):
    def xorOperation(self, n, start):
        #nums[i] = start + 2 * i(indexed)
        nums = []
        for i in range(0,n):
            nums.append(start + 2 * i)

        return nums[]

        
x = Solution()
print(x.xorOperation(5,0))
