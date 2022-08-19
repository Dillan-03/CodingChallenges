# Count odd Number in given range 
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 !=0 and high%2 !=0:
            # both numbers are even/odd
            count = (high-low)//2
            return count+1
        else:
            # # one number is odd and the other is even
            count = (1+(high-low))//2
            return count  

x = Solution()
print(x.countOdds(3,7))