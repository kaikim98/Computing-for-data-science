def P4(nums):
    ans = 0
    for i in nums:
        ans ^= i
    ans &= -ans
    ans1, ans2= 0, 0

    for i in nums:
        if i & ans >0:
            ans1 = ans1 ^ i
        else:
            ans2 = ans2 ^ i
    x = set([ans1, ans2])
    return x