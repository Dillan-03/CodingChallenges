# Two Sum

class Solution:
    def twoSum(self, nums, target: int):
        
        total = [] 
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    total.append(i)
                    total.append(j)
                    return total
        return total
                    
            

x = Solution() 
print(x.twoSum([3,2,4],6))
