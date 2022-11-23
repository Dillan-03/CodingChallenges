#Day of the year
class Solution:
    def dayOfYear(self, date: str) -> int:
        print(list(date))
        if (date[-2] == '0'):
            return(date[-1])
        else:
            return(date[-2]+date[-1])


x = Solution()
print(x.dayOfYear("2019-02-10"))