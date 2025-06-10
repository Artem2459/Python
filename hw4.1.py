def move_zeros_to_end(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


print(move_zeros_to_end([0, 1, 0, 12, 3]))
print(move_zeros_to_end([0]))
print(move_zeros_to_end([1, 0, 13, 0, 0, 0, 5]))
print(move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))

