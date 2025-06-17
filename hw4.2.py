def calculate(nums):
    if not nums:
        return 0
    sum_even_indices = sum(nums[i] for i in range(0, len(nums), 2))
    return sum_even_indices * nums[-1]


print(calculate([0, 1, 7, 2, 4, 8]))
print(calculate([1, 3, 5]))
print(calculate([6]))
print(calculate([]))
