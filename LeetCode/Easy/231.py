#Power of Two
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            return (math.log2(n).is_integer())
        else:
            return False
        
        


x = Solution()
print(x.isPowerOfTwo(0))