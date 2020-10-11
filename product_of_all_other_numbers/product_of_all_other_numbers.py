'''
Input: a List of integers
Returns: a List of integers
'''

import math


def product_of_all_other_numbers(arr):
    # Your code here

    # go through array
    # except current index,
    # create new list without value at current index
    # multiply all numbers in new list

    deleted = 0
    result = []
    for i in range(len(arr)):
        deleted = arr[i]
        arr.pop(i)
        product = math.prod(arr)
        result.append(product)
        arr.insert(i, deleted)
    print(result)


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
