import random


length = random.randint(3, 10)
original_list = [random.randint(1, 20) for _ in range(length)]
print("Початковий список:", original_list)

new_list = [original_list[0], original_list[2], original_list[-2]]
print("Новий список:", new_list)
