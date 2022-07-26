def containsDuplicate(nums):
    dict = {}
    res = False
    for x in nums:
        if dict.get(x) == x:
            res = True
            break
        else:
            dict[x] = x

    return res


nums = [0, 4, 5, 0, 3, 6]

print(containsDuplicate(nums))
