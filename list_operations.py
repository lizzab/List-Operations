# Ben Lizza
# 02/10/20
# List Operations/ METHODS


def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


def product_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return num


def mean_list(numbers):
    return sum(numbers) / len(numbers)


def mode(numbers):
    if numbers == []:
        return None
    else:
        return max(set(numbers), key=numbers.count)




