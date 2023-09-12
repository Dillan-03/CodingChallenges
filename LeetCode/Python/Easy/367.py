# Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        for i in range(1, num):
            if i**2 == num:
                return True
            elif i**2 > num:
                return False
        return False


x = Solution()
print(x.isPerfectSquare(16))
