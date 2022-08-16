class Solution:
    def maximumWealth(self, accounts):
        wealthiest = 0
        for i in accounts:
            
            x = sum(i)
            if (x > wealthiest):
                wealthiest = x

        return wealthiest

x = Solution()
print(x.maximumWealth([[1,2,3],[3,2,1]]))