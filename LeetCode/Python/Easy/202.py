# Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n != 1:
            # if n < 10:
            #     return False
            n = [int(x)*int(x) for x in list(str(n))]
            n = sum(n)
            
        return True

x = Solution()
print(x.isHappy(2))
