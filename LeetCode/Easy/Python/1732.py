#Highest Altitude
class Solution:
    def largestAltitude(self, gain):

        total = []

        for i in range(0,len(gain)+1):
            total.append(sum(gain[:i]))

        return max(total)

gain = [-5,1,5,0,-7]
x = Solution() 
print(x.largestAltitude(gain))
