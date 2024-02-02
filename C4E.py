# 4.1
def recursive_sum(nums):
    value = nums.pop(0)

    if len(nums) == 0:
        return value

    return value + recursive_sum(nums)


numbers = [1, 1, 1, 1, 1, 1]
print(recursive_sum(numbers.copy()))


# 4.2
def count_items_in_list(list):
    list.pop(0)

    if len(list) == 0:
        return 1

    return 1 + count_items_in_list(list)


print(count_items_in_list(numbers.copy()))
