# 4.1
def recursive_sum(nums):
    value = nums.pop(0)

    if len(nums) == 0:
        return value

    return value + recursive_sum(nums)


numbers = [2, 4, 6]
print(recursive_sum(numbers))
