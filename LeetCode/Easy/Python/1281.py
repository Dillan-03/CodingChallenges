#  Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        holder = [int(x) for x in str(n)]
        total = 1
        for i in holder:
            total*=i
        return total - sum(holder)


x = Solution()
print(x.subtractProductAndSum(234))