# Ben Lizza
# 02/11/20
# CONSOLE

import list_operations

numbers = []
print("Enter five values for me to manipulate.")

for num in range(0,5):
    num = int(input())
    numbers.append(num)

numbers.sort()
print(f"This is your list after being sorted: {numbers}")

print(f"The sum of your list is: {list_operations.sum_list(numbers)}")

print(f"This is the product of your list: {list_operations.product_list(numbers)}")
