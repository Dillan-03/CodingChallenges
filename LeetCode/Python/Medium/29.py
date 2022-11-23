#  Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        counter = 0

        if (dividend > 0 and divisor > 0):
            while dividend >= 0 and (dividend-divisor)>=0:
                dividend -= divisor
                counter += 1
        elif (dividend > 0 and divisor < 0):
            while dividend >= 0 and (dividend+divisor)>=0:
                dividend += divisor
                counter += 1
            counter = 0 - counter
        elif (dividend < 0 and divisor > 0):
            while dividend >= 0 and (dividend+divisor)<=0:
                dividend += divisor
                # print(dividend)
                counter += 1
            counter = 0 - counter
        elif (dividend <= 0 and divisor <= 0):
            while dividend < 0 and (dividend-divisor)<=0:
                    dividend -= divisor
                    counter += 1


        return counter

x = Solution()
print(x.divide(-1,1))
