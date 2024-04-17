# 5. Написать функцию, которая возвращает true, если в списке идёт подряд два
# раза заданное число.
# Если заданное число 2, то [1, 2, 2] -> true, [2, 1, 2] -> false

def has_two_consecutive(nums, target):
    for i in range(len(nums) - 1):
        if nums[i] == target == nums[i + 1]:
            return True
    return False


a = [1, 2, 3, 2, 4, 5, 6, 7, 8, 9]
rep = 2
print(has_two_consecutive(a, rep))
