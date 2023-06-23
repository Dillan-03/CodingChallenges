#Binary Search
class Solution:
    def search(self, nums, target) -> int:

        lo = 0
        hi = len(nums)
        step = 0

        if hi < lo:
            return -1

        while lo<=hi:

            # print("Subarray in step {}: {}".format(step,str(nums[lo:hi+1])))
            step+=1

            mid = (lo + hi) // 2

            try:
                if target == nums[mid]:
                    return mid
            except IndexError:
                return -1

            if target < nums[mid]:
                hi = mid -1
            else:
                lo = mid + 1

        return -1
x = Solution()
print(x.search([-1,0,3,5,9,12],9))
   