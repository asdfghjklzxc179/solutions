'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # planning:
    # sort,
    # if n != n+1, return n

    # if integer == arr[index+1] and arr[index+1] is not None:
    # arr.remove(integer)
    # arr.pop(index)
    # return arr[-1]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 2, 2, 6, 3, 3, 9, 0, 0, 9]

    print(f"The odd-number-out is {single_number(arr)}")
