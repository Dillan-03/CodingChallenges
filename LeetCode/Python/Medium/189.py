#Rotate Array 


class Solution:
    def rotate(self, nums, k: int) -> None:
        # while k > 0:
        for shift in range(len(nums)):
            if nums[shift] == nums[-1]:
                nums[0] = nums[shift]
            else:
                print(nums[shift])
            
            # k -= 1
        print(nums)
        

x = Solution()
print(x.rotate([1,2,3,4,5,6,7],1))