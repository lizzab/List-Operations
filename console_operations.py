# Ben Lizza
# 02/11/20
# CONSOLE

import statistics
import list_operations
# Make the user input 5 values that will be put into a list and manipulated
numbers = []
print("Enter five values for me to manipulate.")

for num in range(0,5):
    num = int(input())
    numbers.append(num)

numbers.sort()
print(f"This is your list after being sorted: {numbers}")

print(f"The sum of your list is: {list_operations.sum_list(numbers)}")

print(f"This is the product of your list: {list_operations.product_list(numbers)}")

print(f"This is the average: {list_operations.mean_list(numbers)}")

print(f"This is the median of your list: {numbers[2]}")

if statistics.mode(numbers) == range[0,100]:
    print(f"This is the mode: {statistics.mode(numbers)}")
else:
    print("There's not a mode for the five values you gave me.")
