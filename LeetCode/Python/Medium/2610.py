# 2610. Convert an Array Into a 2D Array With Conditions


def findMatrix(nums):
    print(nums)
    nums = (set(nums))
    print(nums)
    nums = list(nums)
    print(nums)
    temp = [] 

    for numbers in nums:
        if numbers not in temp:
            temp.append(numbers)
            print(temp)
        




findMatrix([1,3,4,1,2,3,1])