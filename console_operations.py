# Ben Lizza
# 02/11/20
# CONSOLE

import list_operations
# Make the user input 5 values that will be put into a list and manipulated

numbers = []
print("Enter five values for me to manipulate.")

for num in range(0,5):
    num = int(input())
    numbers.append(num)

numbers.sort()
print(f"\nThis is your list after being sorted: {numbers}")

print(f"\nThe sum of your list is: {list_operations.sum_list(numbers)}")

print(f"\nThis is the product of your list: {list_operations.product_list(numbers)}")

print(f"\nThis is the average: {list_operations.mean_list(numbers)}")

print(f"\nThis is the median of your list: {numbers[2]}")

print(f"\nThis is the mode of the list: {list_operations.mode(numbers)}")

