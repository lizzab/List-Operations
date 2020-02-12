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

print(f"\nThe largest number is: {numbers[-1]}")

print(f"\nThe smallest number is: {numbers[0]}")

numbers = list(set(numbers))
print(f"\nThis is your list without any duplicates: {numbers}")

print("\nThis is your list after even numbers were removed:")
print(list_operations.odd_list(numbers))

print("\nThis is your list after odd numbers were removed:")
print(list_operations.even_list(numbers))


one_more = input("\nType one more number!")
print(one_more)
if one_more in numbers:
    print("Your number is in the list!")
else:
    print("Your number is not in the list :(")
