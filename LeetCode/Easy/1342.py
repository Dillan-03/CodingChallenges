# Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if (num % 2 == 0):
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps

x = Solution()
print(x.numberOfSteps(14))