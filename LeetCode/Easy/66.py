#Plus One
class Solution:
    def plusOne(self, digits):
        digits[-1] = digits[-1] + 1
        return digits

x = Solution()
print(x.plusOne([1,2,3]))