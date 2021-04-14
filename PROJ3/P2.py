def P2(nums):
    change = True
    while change:
        if len(nums) == 0:
            change = False
        elif len(nums)/2 < sum(nums) and nums[0]== 1:
            del nums[0]
        elif len(nums)/2 < sum(nums) and nums[-1]== 1:
            del nums[-1]
        elif len(nums)/2 < sum(nums) and nums[-1]== 0 and nums[0]==0:
            del nums[-1]
        elif len(nums)/2 > sum(nums) and nums[0]== 0:
            del nums[0]
        elif len(nums)/2 > sum(nums) and nums[-1]== 0:
            del nums[-1]
        elif len(nums)/2 > sum(nums) and nums[-1]== 1 and nums[0]==1:
            del nums[-1]
        elif len(nums)/2 == sum(nums):
            change = False
    x = len(nums)
    return x